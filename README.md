# 👶 BabyBot

**BabyBot** is a simple, local-first web app that provides baby health advice based on age using a GraphQL API. It’s built with FastAPI, Ariadne, SQLModel, and basic HTML+JS. It's LLM-ready and Docker-deployable.

---

## 🚀 Features

- ➕ Add baby profiles (name, age, notes)
- 💡 Get personalized baby health advice (age-based)
- ⚡ FastAPI + Ariadne GraphQL backend
- 🌐 HTML + JS frontend (basic UI)
- 🗃️ SQLite database (file-based or in-memory)
- 🐳 Docker support for easy deployment
- 🔒 Local-first, no external APIs

---

## 🧠 Tech Stack

- **Backend**: FastAPI + Ariadne (GraphQL)
- **Database**: SQLite via SQLModel
- **Frontend**: HTML + JavaScript
- **Optional**: Docker, GitHub, LLM integration (mock)

---

## 🛠️ Getting Started

### 📦 Requirements

- Python 3.11+
- Docker (optional)

---

### ⚙️ Setup Locally

1. **Clone the Repo**

```bash
git clone https://github.com/your-username/babybot.git
cd babybot
```

2. **Create Virtual Environment**

python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows


3. **Install Requirements**

pip install -r requirements.txt


4. **Run the App**

uvicorn app.main:app --reload


5. **Open in browser:**
👉 http://localhost:8000

6. **🧪 Try It Out**
🔍 GraphQL Playground

Visit:
👉 http://localhost:8000/graphql

Example Query:

query {
  babyLLMAdvice(id: 1) {
    advice
  }
}

🐳 Docker Instructions

Build Docker Image

docker build -t baby-advice-app:latest .


Run Docker Container

docker run -p 8000:8000 baby-advice-app:latest


Then open:
👉 http://localhost:8000

🗂️ Project Structure
babybot/
│
├── app/
│   ├── main.py              # FastAPI app entry
│   ├── schema.graphql       # GraphQL schema
│   ├── models.py            # SQLModel definitions
│   ├── db.py                # DB engine and session
│   ├── resolvers.py         # GraphQL resolvers
│   ├── simulate_llm.py      # Mock LLM response
│   └── templates/
│       └── index.html       # Frontend page
│
├── requirements.txt
├── Dockerfile
├── README.md
└── .gitignore

📦 Requirements
fastapi
uvicorn
ariadne
sqlmodel
aiofiles
python-multipart
requests

👀 Screenshots
Frontend (Form)	GraphQL Playground

	
🙋 FAQ

Q: Is this app using an actual LLM?
A: No. It uses a mocked simulate_llm_response() method which you can later replace with OpenAI or other LLMs.

Q: Where is data stored?
A: In a local SQLite DB file at app/db/babybot.db.

Q: How do I reset the database?
A: Delete the DB file and restart the app.