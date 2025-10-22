import streamlit as st
import pandas as pd
import io
import os
from parser import parse_statement
from regex_patterns import REGEX_TEMPLATES

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # Ignore if .env handling isn't needed

def main():
    """Streamlit UI for PDF upload, parsing (RegEx + LLM fallback), and result display."""
    
    gemini_api_key = os.environ.get('GEMINI_API_KEY')
    
    st.set_page_config(page_title="Multi-Bank Statement Parser", layout="centered")
    st.title("💳 Credit Card Statement Parser")
    
    supported_banks = ', '.join(k.upper() for k in REGEX_TEMPLATES.keys())
    st.markdown(f"Upload a credit card statement (PDF) from **{supported_banks}** to extract key details.")
    st.markdown("---")

    is_key_valid = gemini_api_key and gemini_api_key != "YOUR_GEMINI_API_KEY"
    if not is_key_valid:
        st.warning("⚠️ **LLM Fallback Disabled:** Missing `GEMINI_API_KEY`. Only RegEx extraction will run.")
    else:
        st.info("💡 **LLM Fallback Enabled:** Gemini will assist if RegEx misses data.")
    st.markdown("---")

    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

    if uploaded_file:
        st.info(f"File uploaded: **{uploaded_file.name}**")

        bytes_data = io.BytesIO(uploaded_file.getvalue())
        with st.spinner('Analyzing PDF and extracting data...'):
            results = parse_statement(bytes_data, api_key=gemini_api_key)

        st.subheader("Extraction Results")

        if results.get("status") == "SUCCESS":
            bank_name = results.get('bank_name', 'N/A')
            method = results.get('extraction_method', 'RegEx')
            st.success(f"✅ Successful! Bank: **{bank_name}** (Method: {method})")

            llm_status = results.get("llm_status", "N/A")
            if "Fallback" in method:
                if llm_status == "SUCCESS":
                    st.toast("LLM filled missing fields.", icon='🤖')
                elif llm_status == "FAILED":
                    st.warning(f"LLM Fallback Error: {results.get('llm_error', 'Failed to get data.')}")
            elif llm_status == "SKIPPED":
                st.info(f"LLM Fallback skipped ({results.get('llm_error', 'Not needed.')})")

            display_data = {
                "Data Point": [
                    "Card Last 4 Digits",
                    "Statement Date",
                    "Payment Due Date",
                    "Total Amount Due",
                    "Minimum Amount Due",
                ],
                "Extracted Value": [
                    results.get("card_last_4_digits", "N/A"),
                    results.get("statement_date", "N/A"),
                    results.get("payment_due_date", "N/A"),
                    results.get("total_due", "N/A"),
                    results.get("min_payment", "N/A"),
                ]
            }

            df = pd.DataFrame(display_data)

            def color_not_found(val):
                """Highlight 'NOT_FOUND' values in red."""
                return 'background-color: #ffe0e0' if 'NOT_FOUND' in str(val) else ''

            st.dataframe(
                df.set_index("Data Point").style.applymap(color_not_found),
                use_container_width=True
            )

            if 'raw_text' in results:
                with st.expander("🔍 View Raw Extracted Text"):
                    st.code(results['raw_text'], language='text', height=300)

        else:
            st.error(f"❌ Extraction Failed: {results.get('reason', 'Unknown error.')}")
            st.warning("Ensure the PDF is readable and from a supported bank.")
            if 'raw_text' in results:
                with st.expander("🔍 View Raw Extracted Text"):
                    st.code(results['raw_text'], language='text', height=300)

if __name__ == "__main__":
    main()
