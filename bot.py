import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Define a command handler. This will be triggered whenever the /start command is sent to the bot.
def start(update, context):
    update.message.reply_text('Hello! Welcome to the Dragon Ball Z Telegram Game Bot. Type /help to see available commands.')

# Define a command handler. This will be triggered whenever the /help command is sent to the bot.
def help(update, context):
    update.message.reply_text('Available commands:\n/start - Start the bot\n/help - Show available commands')

# Define a message handler. This will be triggered whenever the bot receives a text message.
def echo(update, context):
    update.message.reply_text(update.message.text)

def main():
    # Create the Updater and pass it your bot's token.
    updater = Updater("7146430123:AAGoNlsZdiJAqWFixZCNFMTItbpxQQ0Vvo0", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Register command handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # Register message handler
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT, SIGTERM or SIGABRT.
    updater.idle()

if __name__ == '__main__':
    main()
