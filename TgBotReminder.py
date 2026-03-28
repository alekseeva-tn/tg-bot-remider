import telebot
import datetime
import time
import threading
import random

bot = telebot.TeleBot('введите токен')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, 'Привет! Я чат бот, который будет напоминать тебе выполнять задания')
    reminder_thread = threading.Thread(target=send_reminders, args=(message.chat.id,))
    reminder_thread.start()  # запуск потока

@bot.message_handler(commands=['quote'])
def fact_message(message):
    list = ["Мы есть то, что мы делаем изо дня в день. Способность управлять своими поступками формирует характер, а благодаря характеру, человек обретает способность управлять своей жизнью. Аристотель",
            "Полезные привычки формируются за 21 день ежедневного делания.",
            "Не важно, как сильно ты о чем-то мечтаешь, важно, что ты для этого делаешь.",
            "Если вы хотите иметь то, что никогда не имели, вам придётся делать то, что никогда не делали.",
            "Хотите изменить свою жизнь?! Так действуйте, вместо того, чтобы искать оправдания, запираться и притворяться счастливым...",
            "Человек ценен, когда его слова совпадают с его действиями.",
            "Если хочешь что-то делать — делай, а не сотрясай воздух!"]
    random_fact = random.choice(list)
    bot.reply_to(message, f'Цитата на сегодня: {random_fact}')
def send_reminders(chat_id):
    first_rem = "09:00"
    second_rem = "12:00"
    third_rem = "15:00"
    fourth_rem = "18:00"
    while True:
        now = datetime.datetime.now().strftime("%H:%M")
        if now == first_rem or now == second_rem or now == third_rem or now == fourth_rem:
            bot.send_message(chat_id, "Напоминаение для выполнения задания!")
            time.sleep(61)
        time.sleep(1)

bot.polling(none_stop=True)