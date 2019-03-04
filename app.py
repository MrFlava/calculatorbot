import math
import logging
import telegram
import formencode
from local_settings import Token
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, ConversationHandler

def start(bot, update):
    bot.send_message(chat_id = update.message.chat_id, text = 'Здравствуйте! Я бот-калькулятор, благодаря мне вы можете сложить, отнять, умножить или разделить два числа. Напишите  "/calc" для открытия меню доступных операций.' )

def basic_menu(bot, update):
    keyboard_customer = [[InlineKeyboardButton('Узнать сумму', callback_data= 'сумма'),InlineKeyboardButton('Узнать разность', callback_data= 'разность')],[InlineKeyboardButton('Узнать произведение', callback_data= 'произведение'),InlineKeyboardButton('Узнать частное', callback_data= 'частное')]]
    reply_markup = InlineKeyboardMarkup(keyboard_customer)
    update.message.reply_text('Выберите одну из доступных операций.', reply_markup = reply_markup)

def selected_operation(bot,update):
        query = update.callback_query
        callback_list = ['сумма','разность','произведение','частное']
        if any(query.data == i for i in callback_list):
            bot.send_message(text="Хорошо теперь давайте разберемся с переменными. Введите '/a + значение а'. Потом введите '/b + значение b; ",chat_id=query.message.chat_id,message_id=query.message.message_id)
def value_a(bot,update):
     global a
     a = update.message.text.replace('/a', '')
     a  = "".join(a.split())
     bot.send_message(chat_id = update.message.chat_id, text = 'Тогда a = {}'.format(a))
def value_b(bot, update):
    global b
    b = update.message.text.replace('/b', '')
    b  = "".join(b.split())
    bot.send_message(chat_id = update.message.chat_id, text = 'Тогда b = {}'.format(b))
def answers(bot, update):
    bot.send_message(chat_id = update.message.chat_id,text = 'Сумма будет равна = {}'.format(float(a)+float(b)))
    bot.send_message(chat_id = update.message.chat_id, text = 'Разность будет равна = {}'.format(float(a)-float(b)))
    bot.send_message(chat_id = update.message.chat_id, text = 'Произведение будет равно = {}'.format(float(a)*float(b)))
    bot.send_message(chat_id = update.message.chat_id, text = 'Частное будет равно = {}'.format(float(a)/float(b)))
def main():
    updater = Updater(Token)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("calc", basic_menu))
    dp.add_handler(CommandHandler("a", value_a))
    dp.add_handler(CommandHandler("b", value_b))
    dp.add_handler(CommandHandler("ans", answers))
    dp.add_handler(CallbackQueryHandler(selected_operation))
    dp.add_handler(CallbackQueryHandler(answers))
    updater.start_polling()
    updater.idle()
if __name__ == '__main__':
    main()
