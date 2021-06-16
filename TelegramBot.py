from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters
import logging
from telegram.ext import CommandHandler

def startCommandHandler(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a test-bot, please talk to me!")
    logging.info("/start command received")

def helpCommandHander(update, context):
	context.bot.send_message(chat_id=update.effective_chat.id, text="Here are a list of all the commands configured.\n/start\n/help\n/caps sometext")
	logging.info("/help command received")

def capsCommandHandler(update, context):
	# TODO Add an exception handler for when the text was empty
	text_caps = ' '.join(context.args).upper()
	context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)
	logging.info("/caps command received")

def textHandler(update, context):
	context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I can't respond to your messages yet.Type /help for a list of all commands")

updater = Updater(token='1715192581:AAHN2LJ0pUo4lORhR771ywKuL-RhzM0AAa8', use_context=True)
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

# Register handlers
start_handler = CommandHandler('start', startCommandHandler)
dispatcher.add_handler(start_handler)
help_handler = CommandHandler('help', helpCommandHander)
dispatcher.add_handler(help_handler)
caps_handler = CommandHandler('caps', capsCommandHandler)
dispatcher.add_handler(caps_handler)
text_handler = MessageHandler(Filters.text & (~Filters.command), textHandler)
dispatcher.add_handler(text_handler)
updater.start_polling()
