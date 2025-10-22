import streamlit as st
import pandas as pd
import io
import os
from parser import parse_statement
from regex_patterns import REGEX_TEMPLATES
from styles import get_custom_css

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass


def main():
    """Main application with Catppuccin Mocha theme"""
    
    gemini_api_key = os.environ.get('GEMINI_API_KEY')
    
    # Page config
    st.set_page_config(
        page_title="Smart Credit Card Statement Parser",
        page_icon="💳",
        layout="wide",
        initial_sidebar_state="collapsed"
    )
    
    # Load Catppuccin CSS
    st.markdown(get_custom_css(), unsafe_allow_html=True)
    
    # Header
    st.markdown("""
    <div class="custom-header">
        <h1>💳 Smart Credit Card Statement Parser</h1>
        <p>Extract key financial data from your credit card statements instantly</p>
    </div>
    """, unsafe_allow_html=True)
    
    # API Status
    is_key_valid = gemini_api_key and gemini_api_key != "YOUR_GEMINI_API_KEY"
    
    if not is_key_valid:
        st.markdown("""
        <div class="alert-box alert-warning">
            <span>⚠️</span>
            <span><strong>LLM Fallback Disabled:</strong> Missing GEMINI_API_KEY. Only RegEx extraction will run.</span>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="alert-box alert-success">
            <span>✅</span>
            <span><strong>LLM Fallback Enabled:</strong> Gemini AI will assist if RegEx misses data.</span>
        </div>
        """, unsafe_allow_html=True)
    
    # Features Section
    st.markdown('<p class="section-header">✨ Key Features</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="feature-grid">
        <div class="feature-card">
            <h4>⚡ Lightning Fast</h4>
            <p>Extract data in seconds with advanced RegEx patterns and AI assistance</p>
        </div>
        <div class="feature-card">
            <h4>🤖 AI-Powered Fallback</h4>
            <p>Gemini AI automatically fills missing fields when needed</p>
        </div>
        <div class="feature-card">
            <h4>🔒 Secure & Private</h4>
            <p>Your financial data is processed locally and never stored</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Supported Banks Section
    st.markdown('<p class="section-header">🏦 Supported Banks</p>', unsafe_allow_html=True)
    
    bank_names = {
        'hdfc': 'HDFC Bank',
        'axis': 'Axis Bank',
        'icici': 'ICICI Bank',
        'idfc': 'IDFC First Bank',
        'yes': 'YES Bank'
    }
    
    banks_html = ''.join([f'<div class="bank-card"><p>{name}</p></div>' 
                          for name in bank_names.values()])
    
    st.markdown(f"""
    <div class="bank-grid">
        {banks_html}
    </div>
    """, unsafe_allow_html=True)
    
    # Upload Section
    st.markdown('<p class="section-header">📤 Upload Your Statement</p>', unsafe_allow_html=True)
    
    # File uploader - now fully clickable
    uploaded_file = st.file_uploader(
        "Drag and Drop Your PDF Here",
        type="pdf",
        help="Upload a credit card statement PDF from supported banks"
    )
    
    if uploaded_file:
        st.markdown(f"""
        <div class="alert-box alert-info">
            <span>📄</span>
            <span><strong>File uploaded:</strong> {uploaded_file.name} ({uploaded_file.size / 1024:.1f} KB)</span>
        </div>
        """, unsafe_allow_html=True)
        
        bytes_data = io.BytesIO(uploaded_file.getvalue())
        
        with st.spinner('🔄 Analyzing PDF and extracting data...'):
            results = parse_statement(bytes_data, api_key=gemini_api_key)
        
        # Display Results
        st.markdown('<p class="section-header">📊 Extraction Results</p>', unsafe_allow_html=True)
        
        if results.get("status") == "SUCCESS":
            bank_name = results.get('bank_name', 'N/A')
            method = results.get('extraction_method', 'RegEx')
            
            # Success Banner
            st.markdown(f"""
            <div class="success-banner">
                <h3>✅ Extraction Successful!</h3>
                <p><strong>Bank:</strong> {bank_name} | <strong>Method:</strong> {method}</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Get extracted data
            card_digits = results.get('card_last_4_digits', 'N/A')
            statement_date = results.get('statement_date', 'N/A')
            due_date = results.get('payment_due_date', 'N/A')
            total_due = results.get('total_due', 'N/A')
            min_payment = results.get('min_payment', 'N/A')
            
            # Detailed Table Section
            st.markdown("### 📋 Detailed Information")
            
            # Create HTML table with Catppuccin colors
            table_html = f"""
            <table style="width: 100%; border-collapse: separate; border-spacing: 0; margin: 1.5rem 0; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 15px rgba(0,0,0,0.4);">
                <thead>
                    <tr style="background: linear-gradient(135deg, #cba6f7 0%, #89b4fa 100%);">
                        <th style="color: #11111b; padding: 1rem; text-align: left; font-weight: 600; font-size: 1rem; width: 35%;">Field</th>
                        <th style="color: #11111b; padding: 1rem; text-align: left; font-weight: 600; font-size: 1rem;">Extracted Value</th>
                    </tr>
                </thead>
                <tbody>
                    <tr style="background: {'#313244' if bank_name != 'N/A' else '#45475a'};">
                        <td style="padding: 0.9rem 1rem; border-bottom: 1px solid #45475a; color: {'#a6e3a1' if bank_name != 'N/A' else '#f38ba8'}; font-weight: 500;">🏦 Bank Name</td>
                        <td style="padding: 0.9rem 1rem; border-bottom: 1px solid #45475a; color: {'#cdd6f4' if bank_name != 'N/A' else '#f38ba8'}; font-weight: 600;">{bank_name}</td>
                    </tr>
                    <tr style="background: {'#313244' if card_digits != 'NOT_FOUND' else '#45475a'};">
                        <td style="padding: 0.9rem 1rem; border-bottom: 1px solid #45475a; color: {'#a6e3a1' if card_digits != 'NOT_FOUND' else '#f38ba8'}; font-weight: 500;">💳 Card Last 4 Digits</td>
                        <td style="padding: 0.9rem 1rem; border-bottom: 1px solid #45475a; color: {'#cdd6f4' if card_digits != 'NOT_FOUND' else '#f38ba8'}; font-weight: 600;">{'❌ NOT FOUND' if card_digits == 'NOT_FOUND' else card_digits}</td>
                    </tr>
                    <tr style="background: {'#313244' if statement_date != 'NOT_FOUND' else '#45475a'};">
                        <td style="padding: 0.9rem 1rem; border-bottom: 1px solid #45475a; color: {'#a6e3a1' if statement_date != 'NOT_FOUND' else '#f38ba8'}; font-weight: 500;">📅 Statement Date</td>
                        <td style="padding: 0.9rem 1rem; border-bottom: 1px solid #45475a; color: {'#cdd6f4' if statement_date != 'NOT_FOUND' else '#f38ba8'}; font-weight: 600;">{'❌ NOT FOUND' if statement_date == 'NOT_FOUND' else statement_date}</td>
                    </tr>
                    <tr style="background: {'#313244' if due_date != 'NOT_FOUND' else '#45475a'};">
                        <td style="padding: 0.9rem 1rem; border-bottom: 1px solid #45475a; color: {'#a6e3a1' if due_date != 'NOT_FOUND' else '#f38ba8'}; font-weight: 500;">⏰ Payment Due Date</td>
                        <td style="padding: 0.9rem 1rem; border-bottom: 1px solid #45475a; color: {'#cdd6f4' if due_date != 'NOT_FOUND' else '#f38ba8'}; font-weight: 600;">{'❌ NOT FOUND' if due_date == 'NOT_FOUND' else due_date}</td>
                    </tr>
                    <tr style="background: {'#313244' if total_due != 'NOT_FOUND' else '#45475a'};">
                        <td style="padding: 0.9rem 1rem; border-bottom: 1px solid #45475a; color: {'#a6e3a1' if total_due != 'NOT_FOUND' else '#f38ba8'}; font-weight: 500;">💰 Total Amount Due</td>
                        <td style="padding: 0.9rem 1rem; border-bottom: 1px solid #45475a; color: {'#cdd6f4' if total_due != 'NOT_FOUND' else '#f38ba8'}; font-weight: 600;">{'❌ NOT FOUND' if total_due == 'NOT_FOUND' else f'₹ {total_due}'}</td>
                    </tr>
                    <tr style="background: {'#313244' if min_payment != 'NOT_FOUND' else '#45475a'};">
                        <td style="padding: 0.9rem 1rem; color: {'#a6e3a1' if min_payment != 'NOT_FOUND' else '#f38ba8'}; font-weight: 500;">💵 Minimum Payment</td>
                        <td style="padding: 0.9rem 1rem; color: {'#cdd6f4' if min_payment != 'NOT_FOUND' else '#f38ba8'}; font-weight: 600;">{'❌ NOT FOUND' if min_payment == 'NOT_FOUND' else f'₹ {min_payment}'}</td>
                    </tr>
                </tbody>
            </table>
            """
            
            st.markdown(table_html, unsafe_allow_html=True)
            
            # LLM Status Info
            llm_status = results.get("llm_status", "N/A")
            
            if llm_status == "SUCCESS":
                st.success("🤖 AI successfully filled missing fields!")
            elif llm_status == "FAILED":
                st.warning(f"⚠️ LLM Fallback Error: {results.get('llm_error', 'Failed to get data.')}")
            elif llm_status == "SKIPPED":
                st.info("ℹ️ LLM fallback was not needed - RegEx extraction was successful!")
        
        else:
            st.markdown(f"""
            <div class="alert-box alert-warning">
                <span>❌</span>
                <span><strong>Extraction Failed:</strong> {results.get('reason', 'Unknown error')}</span>
            </div>
            """, unsafe_allow_html=True)
    
    # Footer
    st.markdown("""
    <div class="custom-footer">
        <p>Built with ❤️ using Streamlit & Gemini AI</p>
        <p>Supports HDFC, Axis, ICICI, IDFC First & YES Bank</p>
        <p><small>© 2025 Smart Statement Parser</small></p>
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
