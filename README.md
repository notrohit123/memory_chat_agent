# 🧠 Memory Chat Agent

An intelligent Streamlit-based chatbot that remembers what you say — both now and later.

This isn’t just another chatbot. `Memory Chat Agent` is an interactive, persona-switching AI companion designed for richer, more human-like conversations. It combines **real-time conversational memory** with **long-term memory retention**, making your interactions feel natural, contextual, and persistent across sessions.

---

## 🚀 Features

### 🔮 Conversational Memory
- Stores complete chat threads for dynamic context-aware replies.
- Displays user and assistant message history live.

### 🧠 Long-Term Memory
- Saves key user messages permanently to recall across sessions.
- Searchable by keywords.
- Exportable in multiple formats (JSON, markdown, text).

### 🎭 Persona Switching
- Switch between AI personalities:
  - `default` – General friendly assistant
  - `therapist` – Supportive, emotionally aware guide
  - `coder` – Technical expert for developer-focused queries

### 🌓 Light / Dark Mode Toggle
- Seamlessly switch visual themes on the fly.

### 🔍 Memory Tools
- Keyword-based search through memory logs.
- Message export to `.txt`, `.md`, `.json`.
- Clear/reset memory with a single click.

### 🧠 AI Thought Visualizer
- Peek into how the AI is thinking with a collapsible “Thought Process” panel.

---

## 📸 Preview

![chat_ui and Long term memory](https://private-user-images.githubusercontent.com/93958059/447290116-e18c1ff6-27b0-4b25-a3da-af7940a3e9e1.jpeg?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDgxMjM4MDUsIm5iZiI6MTc0ODEyMzUwNSwicGF0aCI6Ii85Mzk1ODA1OS80NDcyOTAxMTYtZTE4YzFmZjYtMjdiMC00YjI1LWEzZGEtYWY3OTQwYTNlOWUxLmpwZWc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNTI0JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDUyNFQyMTUxNDVaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1lN2I4YjM3MTc0YTUxNzBkZGEzZTY5N2VjNTQ2ZThiZTU0OGUwMmRkODUxZTFkMDkyYzJhZTA5MTUwZWMzZWFjJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.0EzeHp19hGknCS2VCyXePDG3s4EVw_MNbgNIDZrby98)

![Export Memory](https://private-user-images.githubusercontent.com/93958059/447290145-94c755d1-3ffd-4331-8102-d23c55d5af13.jpeg?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDgxMjM5NDIsIm5iZiI6MTc0ODEyMzY0MiwicGF0aCI6Ii85Mzk1ODA1OS80NDcyOTAxNDUtOTRjNzU1ZDEtM2ZmZC00MzMxLTgxMDItZDIzYzU1ZDVhZjEzLmpwZWc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNTI0JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDUyNFQyMTU0MDJaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1mOWJjYzFkNmNiOWYxYjAwYmM3ZjE5ZjJhYzBkMzNmNTNkN2JhNzcwMGFkMTk0YjFmYzc0YjE0YzBlNjk2NjA4JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.le0m0UxZJ6ktUpwRwPpk2sj8rJno0UBx2BkvJ832TYU)

![Memory search](https://private-user-images.githubusercontent.com/93958059/447290148-4e65005d-a8d7-4c20-a50e-760eedaf4c6c.jpeg?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDgxMjM5NDIsIm5iZiI6MTc0ODEyMzY0MiwicGF0aCI6Ii85Mzk1ODA1OS80NDcyOTAxNDgtNGU2NTAwNWQtYThkNy00YzIwLWE1MGUtNzYwZWVkYWY0YzZjLmpwZWc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNTI0JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDUyNFQyMTU0MDJaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT03MGQ5NTgwZGUxMzNmNzI2YzNkOGRlMWI0NjVjMjIyNzY0OTBiMjBmMDcyMGM3YWY3NzIwMGI5NTZlYmUxMTcyJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.m84BWp0LNrojPoT_r-yfghBl5BWVI3gf3g00i6CYxFo)

---

## 🛠 Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/)
- **Backend**: [OpenAI API](https://platform.openai.com/)
- **Memory Management**: In-memory store + `.txt` file persistence
- **Environment Handling**: `python-dotenv`

---

## 📦 Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/notrohit123/memory_chat_agent.git
cd memory_chat_agent
```

```bash
python -m venv venv
# Activate it

# On Windows:
venv\Scripts\activate

# On Mac/Linux:
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```


Add your env file with

```bash
OPENAI_API_KEY=your-openai-key-here
```

Run the app

```bash
streamlit run main.py
```


 Use Cases

* AI therapist for emotional wellness

* Coding assistant with memory of your errors

* Interview prep bot with long-term feedback

* Customer support agent simulation

* Just a smart friend who remembers



 Feedback & Contributions

If you like this project, feel free to give it a ⭐.
Issues, suggestions, or improvements? Open one or make a pull request.
