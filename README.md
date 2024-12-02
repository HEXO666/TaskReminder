

# 📋 Task Manager with Telegram and Phone Call Reminders

A web-based task management application that helps you stay organized and on time! This app sends task reminders via **Telegram bot messages** and **phone calls** using the Twilio API.  

## 🚀 Features
- 📝 **Task Management**: Add tasks with scheduled times through an easy-to-use web interface.
- 🔔 **Telegram Notifications**: Automatically sends task details and reminders to your Telegram bot.
- 📞 **Phone Call Reminders**: Twilio API integration triggers automated calls to remind you of your tasks.
- 🌐 **Web App Interface**: Clean and responsive interface built with Flask and Bootstrap.
- 🗑️ **Task Clearing**: Quickly clear all tasks and their associated reminders.

---

## 🛠️ Installation & Setup
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/task-manager.git
   cd task-manager
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables**:
   Create a `.env` file in the project directory with the following:
   ```
   BOT_TOKEN=your-telegram-bot-token
   CHAT_ID=your-telegram-chat-id
   TWILIO_ACCOUNT_SID=your-twilio-account-sid
   TWILIO_AUTH_TOKEN=your-twilio-auth-token
   TWILIO_PHONE_NUMBER=your-twilio-phone-number
   RECEIVER_PHONE_NUMBER=your-phone-number
   ```

4. **Run the App**:
   ```bash
   python app.py
   ```
   Access the app at [http://127.0.0.1:5000](http://127.0.0.1:5000).

---

## 🛡️ Usage
1. **Add Tasks**:  
   - Enter the task description and specify the reminder time (only time, date is set as today).  
2. **Receive Notifications**:  
   - Get notified via Telegram at the scheduled time.  
   - Receive a phone call reminder from Twilio.  
3. **Clear Tasks**:  
   - Click "Clear All Tasks" to remove tasks and cancel reminders.

---

## 🖥️ Tech Stack
- **Backend**: Flask, APScheduler
- **Frontend**: HTML, CSS, Bootstrap
- **APIs**: 
  - [Telegram Bot API](https://core.telegram.org/bots/api)  
  - [Twilio API](https://www.twilio.com/docs/usage/api)  

---

## 📞 Twilio Integration
- **Phone Call Reminder**: At the task's time, the app triggers a phone call using the Twilio API.
- **Setup Twilio**:
  - Create a Twilio account at [twilio.com](https://www.twilio.com).
  - Get your Account SID, Auth Token, and a Twilio phone number.
  - Add these details to the `.env` file.

---

## 🤝 Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your improvements.

---

## ⚖️ License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## ⭐ Acknowledgments
- **[Twilio](https://www.twilio.com)** for seamless API integration.
- **[Telegram](https://core.telegram.org/bots/api)** for bot messaging.
- **[APScheduler](https://apscheduler.readthedocs.io/)** for scheduling reminders.
- Inspired by the need to stay organized and on time!
```
