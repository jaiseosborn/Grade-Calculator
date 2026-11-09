# College Grade Calculator 🎓

A beginner-friendly **Python + Streamlit** web app for calculating a weighted course grade from five assignments.

## Features
- Enter five assignment scores (0–100)
- Enter five assignment weights (0–100%)
- Validate that the weights add up to 100%
- Display a weighted average and A–F letter grade
- Show each assignment's contribution and the full formula
- Reset all fields to default values

## How the grade is calculated

`Weighted average = Σ(score × weight / 100)`

Grading scale: A ≥90, B ≥80, C ≥70, D ≥60, F <60.

Example: scores 90, 85, 95, 88, 92 with weights of 20% each produce a **90.00% (A)**.

## Run the app locally

1. Install Python 3.10 or newer.
2. Open a terminal in this project folder.
3. Install dependencies: `python -m pip install -r requirements.txt`
4. Start the app: `python -m streamlit run app.py`
5. Open the local URL shown in the terminal.

## Run automated tests

`python -m unittest -v test_grade_logic.py`

Also manually test the app UI, including validation and Reset (see `TESTING.md`).

## Deploy with GitHub and Streamlit Community Cloud

1. Go to https://github.com and create a repository (for example, `college-grade-calculator`).
2. Upload **all project files** from this folder using **Add file → Upload files**; commit the changes.
3. Go to https://share.streamlit.io and sign in with GitHub.
4. Select **New app**, choose your repository and its main branch, and set the main file path to **`app.py`**.
5. Deploy, then open the public app URL and repeat the manual tests.

Never put passwords or private information in a public GitHub repository.

## What each file does
- `app.py`: user interface, buttons, and displayed results
- `grade_logic.py`: validates data and calculates grades
- `requirements.txt`: Python packages needed by Streamlit Cloud
- `test_grade_logic.py`: automated checks for math and invalid input
- `TESTING.md`: manual verification checklist and report template
- `README.md`: project explanation and setup instructions
