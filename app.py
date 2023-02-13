import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, filters

token ='6293141367:AAForYshseRqGS7AImNjCJjOg0sXbXIA3yw'

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello World!")

def main():
    updater = Updater(token)
    dp = updater.dispatcher
    
    start_handler = CommandHandler("start", start)
    dp.add_handler(start_handler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
