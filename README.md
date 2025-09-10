# CSV Cleaner Lite

A beginner-friendly web app to upload, preview, and clean CSV files — no Excel formulas needed.

## Features
- Upload any `.csv` file (up to 200MB)
- Remove duplicate rows
- Drop rows with missing values
- Normalize column headers (e.g., `First Name` → `first_name`)
- Preview your data before and after cleaning
- Download the cleaned file instantly

## Demo

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

## Built With
- Python
- Pandas
- Streamlit

## Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
