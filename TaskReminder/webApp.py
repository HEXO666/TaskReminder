from flask import Flask, request, render_template, redirect, url_for, flash
from twilio.rest import Client
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.date import DateTrigger
from telegram import Bot
from datetime import datetime, date, timedelta
import asyncio

# Replace with your Twilio credentials
TWILIO_ACCOUNT_SID = ''
TWILIO_AUTH_TOKEN = ''
TWILIO_PHONE_NUMBER = ''  # Twilio-provided phone number
USER_PHONE_NUMBER = ''  # Your personal phone number

# Replace with your bot's token
BOT_TOKEN = ''
# Replace with your chat ID
CHAT_ID = ''

# Flask App
app = Flask(__name__)
app.secret_key = ''  # Used for session management (e.g., flash messages)

# Store tasks (temporary storage)
tasks = []

# APScheduler for reminders
scheduler = BackgroundScheduler()
scheduler.start()

async def send_reminder_to_telegram(task, task_time):
    """
    Sends a reminder to the Telegram bot.
    """
    bot = Bot(token=BOT_TOKEN)
    message = f"🔔 Reminder:\n{task}\n⏰ Time: {task_time}"
    try:
        await bot.send_message(chat_id=CHAT_ID, text=message)
        print(f"Reminder sent successfully to Telegram: {message}")
    except Exception as e:
        print(f"Error sending Telegram reminder: {e}")

def make_phone_call(task):
    """
    Sends a phone call reminder using Twilio.
    """
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    message = f"Hello! This is your reminder for the task: {task}."
    try:
        call = client.calls.create(
            twiml=f'<Response><Say>{message}</Say></Response>',
            to=USER_PHONE_NUMBER,
            from_=TWILIO_PHONE_NUMBER
        )
        print(f"Phone call reminder initiated: {call.sid}")
    except Exception as e:
        print(f"Error sending phone call reminder: {e}")

@app.route('/')
def home():
    """
    Home page: Displays task input and task list.
    """
    return render_template('index.html', tasks=tasks, today=date.today())

@app.route('/add_task', methods=['POST'])
def add_task():
    """
    Add a new task with its time from the form, schedule a reminder, and send it to Telegram and Twilio.
    """
    task = request.form.get('task')
    task_time = request.form.get('time')
    if task and task_time:
        # Combine today's date with user-input time
        full_time = f"{date.today()} {task_time}"
        reminder_time = datetime.strptime(full_time, '%Y-%m-%d %H:%M')
        formatted_time = reminder_time.strftime('%d-%b-%Y %I:%M %p')
        
        tasks.append({'task': task, 'time': formatted_time})
        
        # Schedule Telegram and phone call reminders
        scheduler.add_job(
            asyncio.run,
            args=(send_reminder_to_telegram(task, formatted_time),),
            trigger=DateTrigger(run_date=reminder_time),
            id=f"telegram-reminder-{task}-{task_time}",
            replace_existing=True
        )
        scheduler.add_job(
            make_phone_call,
            args=[task],
            trigger=DateTrigger(run_date=reminder_time),
            id=f"phone-reminder-{task}-{task_time}",
            replace_existing=True
        )
        
        flash(f'Task "{task}" scheduled for {formatted_time}, with reminders set for Telegram and phone call!', 'success')
    else:
        flash('Task and time cannot be empty!', 'danger')
    return redirect(url_for('home'))

@app.route('/clear_tasks')
def clear_tasks():
    """
    Clear all tasks from the list and remove reminders.
    """
    global tasks
    tasks = []
    scheduler.remove_all_jobs()  # Clear all scheduled reminders
    flash('All tasks and reminders cleared!', 'info')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
