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
    update.message.reply_text("Hi, this is echo bot. It will repeat everything you write :D")

def echo(update: Update, context: CallbackContext):
    update.message.reply_text(f"{update.message.text}")
updater.dispatcher.add_handler(CommandHandler("start", start))
updater.dispatcher.add_handler(MessageHandler(Filters.text,echo))
updater.start_polling()
