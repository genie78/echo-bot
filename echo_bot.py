#!/usr/bin/env pyhon3 
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.filters import Filters

TOKEN = ''

updater = Updater(token=TOKEN, use_context=True)

def start(update: Update, context: CallbackContext):
    update.message.reply_text(f"Salam {update.effective_user.first_name}, bu bir exo botdur. Siz nə yazsanız təkrarlayacaq :D")

def echo(update: Update, context: CallbackContext):
    update.message.reply_text(f"{update.message.text}")

def main():
    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(MessageHandler(Filters.text,echo))
    updater.start_polling()
    updater.idle()

if __name__=="__main__":
    main()
