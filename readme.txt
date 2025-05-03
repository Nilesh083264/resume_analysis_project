Resume Analysis Project - Setup Guide & Commands

🔧 Step 1: Create and Activate Virtual Environment (Optional)
-------------------------------------------------------------
# Using conda (recommended)
conda create -n resume_env python=3.10
conda activate resume_env

# Or using venv
python -m venv resume_env
python -m venv resume_env

📦 Step 2: Install Dependencies
-------------------------------
pip install -r requirements.txt

🧠 Step 3: Train the ML Model (One-time)
----------------------------------------
python train_model.py

🚀 Step 4: Run the Streamlit App
-------------------------------
streamlit run app.py

🌍 Visit the local URL shown in the terminal (e.g., http://localhost:8501)

🔍 Step 5: Verify Tesseract Installation
----------------------------------------
# In Command Prompt or PowerShell
tesseract --version

📌 If not recognized:
- Install from: https://github.com/UB-Mannheim/tesseract/wiki
- Add to PATH: C:\Program Files\Tesseract-OCR

🧠 Optional Python Fix (if PyCharm doesn't detect Tesseract)
------------------------------------------------------------
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

⚙️ PyCharm Path Fix
-------------------
- File > Settings > Build, Execution, Deployment > Console > Python Console
- Add Environment Variable:
  Name: PATH
  Value: C:\Program Files\Tesseract-OCR

📁 Supported Resume File Formats
-------------------------------
- PDF (.pdf)
- Word (.docx)
- Image (.png, .jpg)

📊 Features in the Dashboard
----------------------------
- Resume skill extraction using NLP
- Role classification (e.g., Data Scientist, QA Engineer)
- Education gap detection based on year parsing

