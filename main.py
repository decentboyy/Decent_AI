import logging
import telebot

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Telegram Bot Token
TOKEN = '6101196560:AAE9Te6XfIfldcJcqdnh6Yb7SHPVi_z3hRc'

# Create bot instance
bot = telebot.TeleBot(TOKEN)

# Dictionary to store the last message for each chat
last_messages = {}

# Handler for generating auto-responses
@bot.message_handler(func=lambda message: True)
def auto_response(message):
    chat_id = message.chat.id

    # Retrieve the last message in the chat
    last_message = last_messages.get(chat_id)
    if last_message:
        # Generate auto-response based on the last message
        auto_reply = "{last_message.text}"
        bot.reply_to(message, auto_reply)

    # Store the current message as the last message for future reference
    last_messages[chat_id] = message

# Start the Bot
bot.polling()
