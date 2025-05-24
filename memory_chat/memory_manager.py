import json

import json

class MemoryStore:
    def __init__(self):
        self.history = []
        self.long_term_file = "long_term_memory.txt"

    def get_conversation(self):
        return self.history.copy()

    def append_user_message(self, message):
        self.history.append({"role": "user", "content": message})
        self.append_to_long_term_memory(message)

    def append_assistant_message(self, message):
        self.history.append({"role": "assistant", "content": message})

    def clear(self):
        self.history = []

    def export_memory(self, fmt="text"):
        if fmt == "json":
            return json.dumps(self.history, indent=2)
        elif fmt == "markdown":
            return "\n".join([f"**{m['role'].capitalize()}**: {m['content']}" for m in self.history])
        return "\n".join([f"{m['role'].capitalize()}: {m['content']}" for m in self.history])

    def search_memory(self, keyword):
        return [m for m in self.history if keyword.lower() in m['content'].lower()]

    def append_to_long_term_memory(self, message):
        with open(self.long_term_file, "a", encoding="utf-8") as f:
            f.write(f"User said: {message}\n")

    def get_long_term_memory(self):
        try:
            with open(self.long_term_file, "r", encoding="utf-8") as f:
                return f.read()
        except FileNotFoundError:
            return "No long-term memory yet."

memory_store = MemoryStore()
