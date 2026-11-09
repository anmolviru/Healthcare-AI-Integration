# Healthcare AI Integration – Strategic Planning Dashboard

An educational dashboard prototype for planning and assessing AI adoption in healthcare.

## Features
- Healthcare AI use-case inventory
- Rule-based risk register and priority assessment
- SWOT analysis
- Strategic implementation roadmap
- KPI overview
- FastAPI backend with sample demonstration data
- React + Vite frontend

## Important disclaimer
This is an educational planning prototype. It is not a clinical decision-support system and must not be used to diagnose or treat patients. Do not enter real patient data.

## Project structure
```text
Healthcare_AI_Integration/
├── backend/
│   ├── main.py
│   ├── data.py
│   └── requirements.txt
├── frontend/
│   ├── index.html
│   ├── package.json
│   └── src/
│       ├── main.jsx
│       ├── App.jsx
│       └── style.css
└── README.md
```

## Run the backend
Open a terminal in the `backend` folder:
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```
API: http://127.0.0.1:8000  
API documentation: http://127.0.0.1:8000/docs

## Run the frontend
Open a second terminal in the `frontend` folder:
```bash
npm install
npm run dev
```
Open the local URL shown by Vite (normally http://localhost:5173).

The frontend expects the backend at `http://127.0.0.1:8000`.
