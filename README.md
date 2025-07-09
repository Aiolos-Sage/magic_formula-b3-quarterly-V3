# Magic Formula - B3 Ranked Analysis

This Streamlit app implements Joel Greenblatt's Magic Formula for value investing, ranking B3 (Brazilian stock exchange) companies by Earnings Yield and Return on Capital.

## Features

- **Fetches and analyzes quarterly financial data for B3 tickers**
- **Ranks stocks using Magic Formula (Earnings Yield + 0.33 × Return on Capital)**
- **Interactive filtering by report date**
- **Displays positive and negative/zero scoring stocks separately**
- **Supports English and Portuguese**

## How to Run

1. **Clone the repository:**

git clone https://github.com/yourusername/your-repo.git
cd your-repo

text

2. **Install dependencies:**

pip install -r requirements.txt

text

3. **Add your API key:**
- Create a folder named `.streamlit` in your project root.
- Inside `.streamlit`, create a file named `secrets.toml`:
  ```
  API_TOKEN = "your_real_api_key_here"
  ```
- Make sure `.streamlit/secrets.toml` is listed in `.gitignore`.

4. **Run the app:**

streamlit run magic_formula-b3-quarterly-V3.py

text

## File Structure

your-project/
│
├── magic_formula-b3-quarterly-V3.py
├── requirements.txt
├── .gitignore
└── .streamlit/
└── secrets.toml

text

## Deployment

- For Streamlit Cloud, upload your `secrets.toml` via the app UI or keep it in `.streamlit` for local runs.
- The app will not run without a valid API key.

## License

MIT License

---

**Note:** This app is for educational purposes and not financial advice.