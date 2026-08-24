---
name: dsh-deepseek-harness
description: DSH (DeepSeek Harness) port for Antigravity with built-in interactive Web UI dashboard (localhost:8999), deep chain-of-thought mathematical reasoning, and 360-degree autonomous verification.
---

# DSH DeepSeek Harness & UI Dashboard Skill

This skill provides a complete port of the **DSH (DeepSeek Harness)** mathematical reasoning engine and provides a built-in interactive Web UI dashboard.

---

## 🚀 Features

1. **Mathematical Reasoning & Chain-of-Thought Verification**: Ingests raw project goals and breaks them into proven invariant steps.
2. **Built-in Interactive Web UI Dashboard**: Hosted at `http://localhost:8999/` for monitoring invariant metrics, Graphify AST node counts, and live reasoning traces.
3. **Continuous AI-Native SDLC Integration**: Binds directly to Graphify knowledge graphs, Context7 official docs, and the 6-stage lifecycle loop.

---

## 🖥️ Launching the UI Dashboard

Run the built-in UI server:
```bash
python ~/.gemini/config/plugins/ai-native-sdlc/dsh-deepseek/ui_server.py
```
Open `http://localhost:8999/` in any browser.
