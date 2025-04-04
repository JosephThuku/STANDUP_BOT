# 🤖 Daily Standup Bot

A powerful Discord bot to automate **daily standup tracking**, assign **productivity points**, and guide users through the process with a friendly interface. Ideal for remote teams, bootcamps, and communities!

---

## ✨ Features

- 🔔 **Daily Standup Reminder** at 10 AM
- ⏳ **Follow-up Reminder** for non-responders at 12 PM
- 👤 **Tracks who responded**
- 🏆 **Points System** for consistent participation
- 🤖 **Welcomes new members** with a guide
- ❓ **Interactive quiz** explaining how it works
- 💬 **Mentions? Bot replies!** Personalized and fun
- 🌐 Easy to deploy and manage

---

## 📸 Preview

![Bot Preview](https://your-screenshot-url.com) *(optional)*

---

## 🚀 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/standup-bot.git
cd standup-bot
```

### 2. Create `.env` File

```bash
touch .env
```

Add your bot token and IDs:

```
DISCORD_BOT_TOKEN=your_bot_token_here
GUILD_ID=your_guild_id_here
CHANNEL_ID=your_channel_id_here
```

### 3. Install Dependencies

Create a virtual environment (recommended):

```bash
python -m venv env
source env/bin/activate
```

Then install dependencies:

```bash
pip install -r requirements.txt
```

### 4. Enable Privileged Intents

Go to your [Discord Developer Portal](https://discord.com/developers/applications):

- Click your app → **Bot**
- Enable:
  - ✅ SERVER MEMBERS INTENT
  - ✅ MESSAGE CONTENT INTENT
- Save changes.

### 5. Run the Bot

```bash
python main.py
```

---

## 🧠 How It Works

### ✅ Daily Flow

1. At **10:00 AM**, the bot sends a standup prompt:
   - What did you work on yesterday?
   - What will you work on today?
   - Any blockers?

2. Users reply directly in the standup channel.

3. At **12:00 PM**, the bot reminds users who haven't replied.

4. Points are tracked automatically for each response.

---

## 👋 New User Guide

When a new user joins, they receive:

- A **personalized welcome**
- A **simple guide** on how to submit standups
- A command `!how` to take a quick quiz on how the bot works

---

## 🧪 Example Commands (Coming soon)

```bash
!points     → Show your current points
!leaderboard → Show top contributors
!how        → Take a quick quiz on how the standup system works
```

---

## 📦 Built With

- Python 🐍
- discord.py
- APScheduler
- dotenv

---

## 🤝 Contributing

PRs are welcome! Just fork this repo and submit a pull request.

---

## 📄 License

MIT License

---

## 💡 Ideas for Future Improvements

- Web dashboard for standup logs
- Weekly reports
- Slack integration
- AI-generated summaries

