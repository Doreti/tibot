import psycopg2
#import logging
from aiogram.dispatcher.filters import Text
from aiogram import Bot, Dispatcher, executor, types
TOKEN = "2076058091:AAG1cQW5GS08Lb5h0TZTMkIlLgEGmQ5lMBk"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
LIMIT = "2"
def get_data_from_db():
    result_test = []
    try:
        conn = psycopg2.connect(dbname='ti', user='ti_user', password='pgpwd4habr', host='172.22.0.2')
        cur = conn.cursor()
        cur.execute("select  need_to from speciality where speciality='devops';")
        knowledge = cur.fetchone()
        for i in knowledge[0].split(','):
            cur.execute("select  * from first_table where type='" + i + "' order by random() LIMIT "+ LIMIT +";")
            result_test.append(cur.fetchall())
        #records = cur.fetchall()
    except:
        print("ошибка конекта!")
        knowledge = "что-то пошло не так"
    return result_test

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    global this_quiz
    global db_data
    db_data = get_data_from_db()
    this_quiz  = await bot.send_poll(message.chat.id, db_data[0][0][1], [db_data[0][0][2], db_data[0][0][3], db_data[0][0][4], db_data[0][0][5]], type='quiz', correct_option_id=0, is_anonymous=False)
    return this_quiz

@dp.poll_answer_handler()
async def handler_poll_answer(poll_answer: types.PollAnswer):
    # проверяем ответ
    #global this_quiz
    if this_quiz.poll.correct_option_id == poll_answer.option_ids[0]:
        await bot.send_message(poll_answer.user.id, 'Правильно! Идём дальше')
    else:
        await bot.send_message(poll_answer.user.id, 'Жаль, но это неправильный ответ. Двигаемся дальше - может потом повезёт')

    # отправляем следующую викторину
    await bot.send_poll(poll_answer.user.id, db_data[0][1][1], [db_data[0][1][2], db_data[0][1][3], db_data[0][1][4], db_data[0][1][5]], type='quiz', correct_option_id=0, is_anonymous=False)
######################################


@dp.message_handler(commands="devops")
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Да!", "Нет!"]
    keyboard.add(*buttons)
    await message.answer("А кофе будешшш?", reply_markup=keyboard)
@dp.message_handler(lambda message: message.text == "Да!")
async def without_puree(message: types.Message):
    b = get_data_from_db()
    print(b)
    await message.reply(b)
@dp.message_handler(lambda message: message.text == "Нет!")
async def without_puree(message: types.Message):
    await message.reply(type(b))
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
