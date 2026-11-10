# StudyMate AI ✦

A personal AI study assistant: **AI Tutor**, **Notes Summarizer**, **Quiz Generator**, **Flashcards** and **Study History**.
Built with Flask, the Google Gemini API (`google-genai`), SQLite and vanilla HTML/CSS/JS.

## Project structure
| Path | Purpose |
|---|---|
| `app.py` | App factory: creates Flask app, registers routes, inits DB. Render runs `app:app`. |
| `config.py` | Reads settings from environment variables / `.env`. |
| `routes/api.py` | JSON API: validates input, calls Gemini, saves to SQLite. |
| `services/gemini_service.py` | All Gemini calls + prompts (one place for AI logic). |
| `database/db.py` | SQLite connection + schema (`history` table). |
| `templates/index.html` | Dashboard page (sidebar + 6 views). |
| `static/css/style.css` | Blue/purple light theme, responsive. |
| `static/js/app.js` | Frontend logic: fetch API, render results, quiz scoring, flashcard flip. |
| `tests/test_app.py` | Unit tests (Gemini mocked, no key needed). |
| `render.yaml` | Render deployment config. |
| `.env.example` | Template for your secrets. |

## Run locally
```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env            # then paste your key into .env
python app.py                   # open http://127.0.0.1:5000
```
Get a free Gemini key at https://aistudio.google.com/apikey. The key stays on the server; the browser never sees it.

## Testing
Automated (no API key needed):
```bash
python -m unittest discover -s tests -v
```
Manual checklist (with a real key): try each tool, take a quiz (colors + score), flip flashcards, open/delete items in History, test on a phone-width window, and submit empty/too-short input to see error toasts.

## Deploy to GitHub + Render
1. `git init && git add . && git commit -m "StudyMate AI" ` then push to a new GitHub repo (`.env` is git-ignored).
2. On https://render.com: **New → Blueprint** (uses `render.yaml`) or **New → Web Service** with build `pip install -r requirements.txt` and start `gunicorn app:app`.
3. Add env var `GEMINI_API_KEY` in the Render dashboard.
4. Deploy. Health check is `/health`.

> **Note:** Render's free tier has an ephemeral disk, so SQLite history resets on redeploy/restart. Fine for demos. For persistence, add a Render Disk and set `DATABASE_PATH=/var/data/studymate.db`.

## API
`POST /api/tutor` · `/api/summarize` · `/api/quiz` · `/api/flashcards` · `GET /api/history` · `GET|DELETE /api/history/<id>` · `GET /api/stats`
