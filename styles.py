# styles.py

def get_custom_css():
    """Returns the custom CSS with Catppuccin Mocha color theme"""
    return """
    <style>
        /* Import Google Fonts */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
        
        /* Catppuccin Mocha Color Palette */
        :root {
            --ctp-rosewater: #f5e0dc;
            --ctp-flamingo: #f2cdcd;
            --ctp-pink: #f5c2e7;
            --ctp-mauve: #cba6f7;
            --ctp-red: #f38ba8;
            --ctp-maroon: #eba0ac;
            --ctp-peach: #fab387;
            --ctp-yellow: #f9e2af;
            --ctp-green: #a6e3a1;
            --ctp-teal: #94e2d5;
            --ctp-sky: #89dceb;
            --ctp-sapphire: #74c7ec;
            --ctp-blue: #89b4fa;
            --ctp-lavender: #b4befe;
            --ctp-text: #cdd6f4;
            --ctp-subtext1: #bac2de;
            --ctp-subtext0: #a6adc8;
            --ctp-overlay2: #9399b2;
            --ctp-overlay1: #7f849c;
            --ctp-overlay0: #6c7086;
            --ctp-surface2: #585b70;
            --ctp-surface1: #45475a;
            --ctp-surface0: #313244;
            --ctp-base: #1e1e2e;
            --ctp-mantle: #181825;
            --ctp-crust: #11111b;
        }
        
        /* Global Styles */
        * {
            font-family: 'Inter', sans-serif;
        }
        
        /* Hide Streamlit Branding */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        /* Main Container */
        .stApp {
            background-color: var(--ctp-base);
        }
        
        .main .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
            max-width: 1200px;
        }
        
        /* Custom Header */
        .custom-header {
            background: linear-gradient(135deg, var(--ctp-mauve) 0%, var(--ctp-blue) 100%);
            padding: 3rem 2rem;
            border-radius: 20px;
            margin-bottom: 2rem;
            box-shadow: 0 20px 60px rgba(203, 166, 247, 0.3);
            text-align: center;
        }
        
        .custom-header h1 {
            color: var(--ctp-crust);
            font-size: 2.8rem;
            font-weight: 700;
            margin: 0 0 0.5rem 0;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
        }
        
        .custom-header p {
            color: var(--ctp-base);
            font-size: 1.2rem;
            margin: 0;
            font-weight: 500;
        }
        
        /* Section Headers */
        .section-header {
            font-size: 1.5rem;
            font-weight: 700;
            color: var(--ctp-text);
            margin: 2rem 0 1rem 0;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }
        
        /* Feature Cards */
        .feature-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 1.5rem;
            margin: 1.5rem 0;
        }
        
        .feature-card {
            background: var(--ctp-surface0);
            padding: 2rem;
            border-radius: 16px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.3);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            border: 1px solid var(--ctp-surface1);
        }
        
        .feature-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 30px rgba(203, 166, 247, 0.4);
            border-color: var(--ctp-mauve);
        }
        
        .feature-card h4 {
            font-size: 1.1rem;
            font-weight: 600;
            color: var(--ctp-mauve);
            margin: 0 0 0.5rem 0;
        }
        
        .feature-card p {
            font-size: 0.95rem;
            color: var(--ctp-subtext0);
            margin: 0;
            line-height: 1.6;
        }
        
        /* Bank Cards */
        .bank-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
            gap: 1rem;
            margin: 1.5rem 0;
        }
        
        .bank-card {
            background: linear-gradient(135deg, var(--ctp-sapphire) 0%, var(--ctp-blue) 100%);
            padding: 1.5rem;
            border-radius: 12px;
            text-align: center;
            box-shadow: 0 4px 15px rgba(116, 199, 236, 0.4);
            transition: transform 0.3s ease;
        }
        
        .bank-card:hover {
            transform: scale(1.05);
            box-shadow: 0 6px 20px rgba(137, 180, 250, 0.5);
        }
        
        .bank-card p {
            color: var(--ctp-crust);
            font-weight: 600;
            font-size: 0.95rem;
            margin: 0;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        
        /* Alert Boxes */
        .alert-box {
            padding: 1rem 1.5rem;
            border-radius: 12px;
            margin: 1rem 0;
            display: flex;
            align-items: center;
            gap: 0.75rem;
            font-size: 0.95rem;
        }
        
        .alert-success {
            background: var(--ctp-surface0);
            border-left: 4px solid var(--ctp-green);
            color: var(--ctp-green);
        }
        
        .alert-warning {
            background: var(--ctp-surface0);
            border-left: 4px solid var(--ctp-peach);
            color: var(--ctp-peach);
        }
        
        .alert-info {
            background: var(--ctp-surface0);
            border-left: 4px solid var(--ctp-blue);
            color: var(--ctp-sky);
        }
        
        /* Upload Section - Polished and Clean */
        [data-testid="stFileUploader"] {
            background: var(--ctp-surface0);
            padding: 4rem 2rem;
            border-radius: 20px;
            border: 3px dashed var(--ctp-surface2);
            text-align: center;
            margin: 2rem 0;
            transition: all 0.3s ease;
            cursor: pointer;
        }
        
        [data-testid="stFileUploader"]:hover {
            border-color: var(--ctp-mauve);
            background: var(--ctp-surface1);
            box-shadow: 0 8px 30px rgba(203, 166, 247, 0.3);
        }
        
        [data-testid="stFileUploader"] section {
            padding: 0;
            border: none;
            background: transparent;
        }
        
        [data-testid="stFileUploader"] section > div {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 1rem;
        }
        
        /* Hide the default label and show custom styling */
        [data-testid="stFileUploader"] label {
            font-size: 1.3rem !important;
            color: var(--ctp-text) !important;
            font-weight: 600 !important;
            cursor: pointer;
            display: block !important;
            margin: 0 !important;
            padding: 0 !important;
        }
        
        /* Style the file input area */
        [data-testid="stFileUploader"] [data-testid="stFileUploaderDropzone"] {
            background: transparent !important;
            border: none !important;
            padding: 0 !important;
        }
        
        [data-testid="stFileUploader"] [data-testid="stFileUploaderDropzoneInput"] {
            cursor: pointer !important;
        }
        
        /* Hide the browse files button */
        [data-testid="stFileUploader"] button {
            display: none !important;
        }
        
        /* Style the help text */
        [data-testid="stFileUploader"] small {
            color: var(--ctp-overlay0) !important;
            font-size: 0.85rem !important;
            margin-top: 1rem !important;
            display: block;
        }
        
        /* Success Banner */
        .success-banner {
            background: linear-gradient(135deg, var(--ctp-green) 0%, var(--ctp-teal) 100%);
            color: var(--ctp-crust);
            padding: 1.5rem 2rem;
            border-radius: 16px;
            margin-bottom: 2rem;
            box-shadow: 0 8px 25px rgba(166, 227, 161, 0.4);
        }
        
        .success-banner h3 {
            font-size: 1.5rem;
            margin: 0 0 0.5rem 0;
            font-weight: 700;
            color: var(--ctp-base);
        }
        
        .success-banner p {
            margin: 0;
            font-size: 1rem;
            color: var(--ctp-base);
            font-weight: 500;
        }
        
        /* Footer */
        .custom-footer {
            text-align: center;
            padding: 2rem;
            color: var(--ctp-overlay0);
            border-top: 1px solid var(--ctp-surface0);
            margin-top: 4rem;
        }
        
        .custom-footer p {
            margin: 0.5rem 0;
            font-size: 0.9rem;
        }
        
        /* Button Styling */
        .stButton>button {
            background: linear-gradient(135deg, var(--ctp-mauve) 0%, var(--ctp-blue) 100%);
            color: var(--ctp-base);
            border: none;
            border-radius: 10px;
            padding: 0.75rem 2rem;
            font-weight: 600;
            font-size: 1rem;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(203, 166, 247, 0.3);
        }
        
        .stButton>button:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 25px rgba(203, 166, 247, 0.5);
        }
        
        /* Streamlit Elements */
        .stSpinner > div {
            border-top-color: var(--ctp-mauve) !important;
        }
        
        /* Info/Success/Warning/Error boxes */
        .stAlert {
            background-color: var(--ctp-surface0) !important;
            color: var(--ctp-text) !important;
            border-radius: 10px !important;
        }
        
        /* Responsive Design */
        @media (max-width: 768px) {
            .custom-header h1 {
                font-size: 2rem;
            }
            
            .feature-grid, .bank-grid {
                grid-template-columns: 1fr;
            }
            
            [data-testid="stFileUploader"] {
                padding: 3rem 1.5rem;
            }
        }
    </style>
    """
