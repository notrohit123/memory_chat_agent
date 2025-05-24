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

![chat_ui](assets/chat_preview.png)

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
