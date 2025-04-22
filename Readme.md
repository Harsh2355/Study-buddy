# 🧠 Slide Explainer AI

This is a Python CLI tool that allows users—especially students—to deeply explore and understand slides from a PDF presentation using OpenAI's `gpt-4o` model. It processes each slide as an image and generates rich, educational explanations based on the visual content and a detailed instructional prompt.

---

## 📦 Features

- 📖 **Step-through Slide Navigation**  
  Move forward, backward, or jump to any slide in your PDF.

- 📚 **In-depth AI Explanations**  
  Get comprehensive, well-structured, and educational breakdowns of each slide’s content.

- 🧑‍🏫 **Custom Prompting**  
  Prompts are designed as if the AI were a knowledgeable computer science professor.

- ❓ **Ask Questions Freely**  
  Ask questions during navigation and get answers directly from GPT.

- 🖼️ **Image Processing**  
  Each slide is converted to an image and fed into the GPT-4o model with visual support.

---

## 🛠️ Requirements

- Python 3.7+
- `pymupdf` (for PDF processing)
- `openai` (OpenAI API)
- Your own OpenAI API credentials
- `static_prompts.py` (included or customizable)

---

## 📂 File Structure

```
project/
│
├── study.py         # Main CLI script
├── static_prompts.py          # Prompt constants
├── README.md                  # You're here
```

---

## ▶️ How to Use

### 1. Install Dependencies

```bash
pip install pymupdf openai
```

### 2. Set Up OpenAI Key

Make sure your OpenAI API key is configured properly, e.g. via environment variable:

```bash
export OPENAI_API_KEY=your-key-here
```

### 3. Run the Script

```bash
python slide_explainer.py your_presentation.pdf
```

### 4. Commands In-App

| Command | Action |
|--------|--------|
| `n` | Next Slide |
| `b` | Batch multiple slides together |
| `p` | Previous Slide |
| `s` | Skip current slide |
| `a` | Ask a custom question |
| `g` | Go to a specific page |
| `q` | Quit |

---

## 🧠 Prompt Structure

This tool uses two prompts:

- **System Prompt**: Frames GPT as a knowledgeable CS professor.
- **User Prompt**: Asks for thorough explanations with analogies, examples, misconceptions, diagrams, and more.

These are stored in `static_prompts.py` and can be modified for other domains or levels of depth.

---

## 💡 Example Use Cases

- Study assistant for difficult lecture slides.
- Revision tool for course material.
- Tutoring aid for complex visual content.
- Self-paced learning assistant.

---

## 📝 To-Do / Future Enhancements

- [ ] GUI version for easier navigation
- [ ] Save/Export explanations to markdown or PDF
- [ ] Multi-slide comparison analysis

---

## 🧾 License

MIT – free to use and modify. If you use this in a project, a shoutout would be awesome! 🚀