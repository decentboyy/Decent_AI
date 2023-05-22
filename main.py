import pyrogram
from pyrogram import filters
from pymongo import MongoClient

# Initialize the Pyrogram client
app = pyrogram.Client(
    "my_bot",
    api_id="18654447",
    api_hash="60ac6f65c766e73dfcc1debef93d06bc",
    bot_token="5058249365:AAHVL7ozsLYA6N3dHtUTAVkZ3sv_YniZdOk"
)

# Connect to MongoDB
mongo_client = MongoClient("mongodb+srv://abc:abcd@cluster0.0g1g1gt.mongodb.net/?retryWrites=true&w=majority")
db = mongo_client["chatbot_db"]

# Handler for incoming messages
@app.on_message(filters.text)
def handle_message(client, message):
    # Get the chat ID
    chat_id = message.chat.id

    # Get or create the chat document in the database
    chat = db.chats.find_one({"chat_id": chat_id})
    if not chat:
        chat = {"chat_id": chat_id, "data": message.text}
        db.chats.insert_one(chat)
        reply_text = "Hello! How can I assist you today?"
    else:
        # Retrieve the data associated with the chat
        data = chat["data"]

        # Process the incoming message and generate a reply
        # Replace this with your AI model or any other logic
        reply_text = f"You said: {message.text}. Your data: {data}"

        # Update the data in the database
        db.chats.update_one({"chat_id": chat_id}, {"$set": {"data": message.text}})

    # Send the reply
    client.send_message(chat_id, reply_text)

# Start the bot
app.run()
