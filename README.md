# CSV Cleaner Lite

A beginner-friendly web app to upload, preview, and clean CSV files — no Excel formulas needed.

## Features
- Upload any `.csv` file (up to 200MB)
- Instantly preview your data
- One-click cleaning options:
  - Remove duplicate rows
  - Drop rows with missing values
  - Normalize column headers
- Download the cleaned file instantly

## Demo

### 🚀 Live App
👉 [**CSV Cleaner Lite on Streamlit →**](https://csv-cleaner-lite-4adhqmytxndra7fhsyyrew.streamlit.app)

### 1. Upload a CSV file & Preview the Data
![CSV Upload](screenshots/csv_upload.png)
### 2. Choose Cleaning Options
![Clean Options 1](screenshots/Options1.png)
![Clean Options 2](screenshots/Options2.png)
![Clean Options 3](screenshots/Options3.png)
### 3. Download Cleaned File
![Download Example 1](screenshots/Download1.png)
![Download Example 2](screenshots/Download2.png)

## Freelance Use Case

Perfect for clients who:
- Work with messy spreadsheets
- Need quick data validation
- Want to clean and download data without touching Excel

## How It Works

1. Upload a `.csv` file from your computer.
2. The app reads the file using Python's **Pandas** library.
3. Choose cleaning options:
   - Remove duplicate rows
   - Drop rows with missing values
   - Clean up column names (e.g., `First Name` → `first_name`)
4. Instantly see the results.
5. Click **Download** to save your clean CSV — ready to use for Excel, Sheets, or analysis.

No Excel formulas. No coding. Just click and go.

## Built With
- Python
- Pandas
- Streamlit

## Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
