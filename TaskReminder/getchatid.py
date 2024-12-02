import asyncio
from telegram import Bot

# Replace with your bot's token
BOT_TOKEN = ''

async def get_chat_id():
    """
    Fetches and prints the chat ID for messages sent to the bot.
    """
    bot = Bot(token=BOT_TOKEN)
    print("Send a message to your bot and then run this script.")
    updates = await bot.get_updates()
    for update in updates:
        print(f"Chat ID: {update.message.chat.id}")

# Run the asynchronous function
asyncio.run(get_chat_id())
