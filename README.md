# TaskLens 📌

**Turn university announcements into clear, actionable tasks with AI.**

TaskLens is an AI-powered application that helps students understand university announcements, emails, and notices by converting them into concise summaries, deadlines, task checklists, and required documents.

## 🚀 The Problem

Students often receive long announcements containing important deadlines and instructions. Missing a single detail can lead to missed submissions or incomplete requirements.

## 💡 Our Solution

TaskLens uses **Gemma 4** to analyze announcements and extract useful information in a structured format.

### ✨ Features

- 📝 **Smart Summaries:** Understand the main message quickly.
- 📅 **Deadline Extraction:** Identify deadlines and flag dates that need confirmation.
- ✅ **Action Checklist:** Turn instructions into tasks.
- 📎 **Required Documents:** Identify documents and materials mentioned in the announcement.
- ⚠️ **Uncertainty Detection:** Highlight missing or ambiguous information.
- 🌐 **Language Options:** Choose from the languages supported by the application.

## 🛠️ Technology Stack

- Python
- Streamlit
- Gemma 4 through the Google Gen AI SDK
- Python dotenv for environment configuration

## 💻 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/SaniaMubasher/TaskLens.git
cd TaskLens
```

Replace `YOUR-GITHUB-USERNAME` with your GitHub username.

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure your API key

Create a `.env` file in the project root:

```text
GEMINI_API_KEY=your_actual_api_key
```

Get an API key through [Google AI Studio](https://aistudio.google.com/).

**Never commit your `.env` file or share your API key publicly.**

### 5. Start TaskLens

```bash
streamlit run app.py
```

## 🧠 AI Workflow

1. The user pastes an announcement.
2. Gemma 4 analyzes the text.
3. The application validates and organizes the response.
4. TaskLens displays the summary, deadlines, tasks, documents, and uncertainties.

## 🎯 Vision

Our goal is to help students spend less time interpreting announcements and more time completing their work.

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

**Built for the hackathon community with Gemma 4 and open-source tools.**
