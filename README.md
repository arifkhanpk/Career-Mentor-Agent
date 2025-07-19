# 🎓 Career Mentor Agent (CLI-Based)

A smart multi-agent system to guide users in choosing the right career field. It suggests domains, explains them, provides required skills, and possible job roles using a conversation-style flow — all inside the terminal (CLI).

## 🚀 Features

- 🤖 CLI-based intelligent assistant
- 🧠 Understands user interests and moods
- 🎯 Suggests career fields based on preference
- 📚 Lists required skills per domain
- 💼 Shows job roles in chosen fields
- 💬 Realistic conversational flow (hello ➝ help ➝ suggest ➝ explain ➝ more ➝ exit)
- 🔄 Handoff between multiple agents:
  - `CareerAgent`
  - `SkillAgent`
  - `JobAgent`

## ⚙️ Technologies Used

| Component       | Tech Used         |
|----------------|-------------------|
| Language        | Python 3.10+       |
| LLM             | OpenRouter API via OpenAI SDK |
| Agent SDK       | OpenAI Agent SDK + Runner |
| Env Management  | `python-dotenv` |
| CLI Interface   | Python I/O        |

## 🗂️ Folder Structure

```

career-mentor-cli/
│
├── agents/
│   ├── career\_agent.py      # Suggests fields and summaries
│   ├── skill\_agent.py       # Required skills by field
│   └── job\_agent.py         # Job roles per domain
│
├── app.py                   # Main orchestrator agent with logic
├── runner.py                # Entry point to run the CLI chat
├── .env                     # API keys and config
├── requirements.txt         # Dependencies
└── README.md                # Project documentation

````

## 🛠️ Setup Instructions

### 1️⃣ Create and Activate Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate       # Windows
# OR
source venv/bin/activate    # macOS/Linux
````

### 2️⃣ Install Required Packages

```bash
pip install -r requirements.txt
```

### 3️⃣ Create `.env` File

Create a `.env` file with:

```
OPENAI_API_KEY=your-openrouter-api-key
OPENAI_API_BASE=https://openrouter.ai/api/v1
OPENAI_MODEL=gpt-3.5-turbo
```

## ▶️ How to Run

```bash
python runner.py
```

You'll be greeted by the agent in your terminal:

```
👋 Hello! I'm your Career Mentor Agent.
How can I assist you in choosing the right career path?

👇 Choose a field below:
1. Engineering
2. Medicine
3. Arts & Design
4. Business
5. Computer Science
6. Law
7. Education
...
```

You can then interact with the bot using typed commands like:

* `1` or `engineering`
* `more`
* `ok`, `bye`, `thanks` to exit

## 💬 Example Flow

```
User: hi
Agent: 👋 Hello! I'm your Career Mentor Agent. How can I assist you?
Agent: Please choose a career field:
       1. Engineering
       2. Medicine
       3. Arts & Design

User: Engineering
Agent: Engineering is the application of science and math to solve real-world problems...
Agent: Required skills:
       - Critical thinking
       - Programming
       - Teamwork
Agent: Possible job roles:
       - Software Engineer
       - Civil Engineer
       - Mechanical Engineer
User: more
Agent: Further details about engineering...

User: thank you
Agent: 😊 You're welcome! Best of luck with your career journey. 👋
```

## 🔐 Security Notes

* Your `.env` file is **not pushed to GitHub**.
* Never share your API key publicly.

## 🔄 To-Do / Improvements

* [ ] Add persistent history
* [ ] Add database for saved choices
* [ ] Turn into a Chainlit / Web interface (optional)
* [ ] Multi-language support

