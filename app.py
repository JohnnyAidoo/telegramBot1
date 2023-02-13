import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

token ='6293141367:AAForYshseRqGS7AImNjCJjOg0sXbXIA3yw'

def start(update, context):
    update.message.reply_text('welcome')

def handleText(update, context):
    update.message.reply_text(f"You said {update.message.text}")


def main():
    updater = Updater(token)
    dp = updater.dispatcher
    
    start_handler = CommandHandler("start", start)
    dp.add_handler(start_handler)
    dp.add_handler(MessageHandler(Filters.text, handleText))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
