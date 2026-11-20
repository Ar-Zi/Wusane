# ووشانێ

A Sorani Kurdish letter-building dice game for one human player against the computer, packaged as a Streamlit web app.

## Files

- `wusane_app.py` - Streamlit entry point
- `ووشانێ.html` - complete HTML, CSS, and JavaScript game
- `requirements.txt` - Python dependency list
- `.streamlit/config.toml` - Streamlit theme and server settings
- `.gitignore` - files Git should ignore
- `LICENSE` - MIT licence

## Run locally

1. Install Python 3.10 or newer.
2. Open a terminal in this folder.
3. Create and activate a virtual environment:

   **macOS/Linux**

       python3 -m venv .venv
       source .venv/bin/activate

   **Windows PowerShell**

       py -m venv .venv
       .venv\Scripts\Activate.ps1

4. Install dependencies:

       pip install -r requirements.txt

5. Start the app:

       streamlit run wusane_app.py

The layout adapts to narrow and wide screens. On short screens, scroll the page to
reach all controls.

## Push to a private GitHub repository

Create an empty private repository on GitHub, then run:

    git init
    git add .
    git commit -m "Initial Sorani word game"
    git branch -M main
    git remote add origin YOUR_PRIVATE_REPOSITORY_URL
    git push -u origin main

Do not add API keys or passwords to this repository.

## Deploy with Streamlit Community Cloud

1. Push the project to GitHub.
2. In Streamlit Community Cloud, create a new app.
3. Select the private repository and `wusane_app.py` as the entry point.
4. Deploy.

The game runs in the browser. Game state resets when the page is refreshed.
