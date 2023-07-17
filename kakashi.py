import random
import telebot

# Replace 'YOUR_API_TOKEN' with your Telegram bot API token
TOKEN = '6363103413:AAFJ6KCv9l2llr9UigP5SR-plWsN7RhzJUY'

# Create an instance of the TeleBot class
bot = telebot.TeleBot(TOKEN)

# Define Kakashi-style dialogues
dialogues = [
    "I'm Freakzz, your friendly neighborhood group manager!",
    "Yo! How's the group doing today?",
    "Hmm... seems like we've got some tasks to handle.",
    "Remember, teamwork makes the dream work!",
    "Alright, time to put on our serious faces and get to work.",
    "Believe it! We'll make this group awesome!",
    "Looks like we're ready for another mission.",
    "I'm not lazy, I just do things in the most efficient way possible!",
    "Let's show everyone what we're made of!",
    "Don't underestimate the power of this group.",
    "Alright, let's get down to business!"
]

# Handle '/start' and '/help' commands
@bot.message_handler(commands=['start', 'help'])
def send_greetings(message):
    response = random.choice(dialogues)
    bot.reply_to(message, response)

# Handle new member join event
@bot.message_handler(func=lambda message: message.new_chat_members)
def handle_new_member(message):
    response = "Welcome to the group, new member! I'm Freakzz, your friendly group manager. Let's make this place awesome together!"
    bot.reply_to(message, response)

# Handle member leave event
@bot.message_handler(func=lambda message: message.left_chat_member)
def handle_member_leave(message):
    response = "Goodbye, member! If you ever need us again, don't hesitate to come back!"
    bot.reply_to(message, response)

# Handle custom commands or messages
@bot.message_handler(func=lambda message: True)
def handle_custom_commands(message):
    response = random.choice(dialogues)
    bot.reply_to(message, response)

# Start the bot
bot.polling()
