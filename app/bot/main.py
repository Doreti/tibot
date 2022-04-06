import psycopg2
#import logging
from aiogram.dispatcher.filters import Text
from aiogram import Bot, Dispatcher, executor, types
import random
######
TOKEN = "TOKEN"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
LIMIT = "2"
######
def wright_result(user_id, send_answer, field_knowlage):
    try:
        conn = psycopg2.connect(dbname='ti', user='ti_user', password='pgpwd4habr', host='172.22.0.2')
        cur = conn.cursor()
        cur.execute("update user_list set "+field_knowlage+"='"+send_answer+"' where user_id='"+user_id+"';")
    except:
        print("не смог записать")
    conn.close()
def get_result():
    result = ""
    return result
   
def get_data_from_db(user_id):
    result_test = []
    some_new = []
    try:
        conn = psycopg2.connect(dbname='ti', user='ti_user', password='pgpwd4habr', host='172.22.0.2')
        cur = conn.cursor()
        cur_user = conn.cursor()
        cur.execute("select need_to from speciality where speciality='devops';")
        knowledge = cur.fetchone()
        for i in knowledge[0].split(','):
            cur.execute("select id from first_table where type='" + i + "' order by random() LIMIT "+ LIMIT +";")
            result_test.append(cur.fetchall())
        #records = cur.fetchall()
        for k in result_test:
            for d in k:
                some_new.append(str(d)[1:-2])
    except:
        print("ошибка конекта!")
        knowledge = "что-то пошло не так"
#add new user in data base
    try:
        cur_user.execute("insert into user_list (user_id, linux, git, ansible, postgres, result) values ('"+str(user_id)+"','0','0','0','0','0');")
        conn.commit()
        cur_user.close()
    except:
        print("ошибка конекта!")
    conn.close()
    return some_new

def get_qwestion_from_db(id_name):
    try:
        conn = psycopg2.connect(dbname='ti', user='ti_user', password='pgpwd4habr', host='172.22.0.2')
        cur = conn.cursor()
        cur.execute("select qwestion, answer0, answer1, answer2, answer3 from first_table where id='"+id_name+"';")
        qwestion = cur.fetchone()
        
    except:
        print("ошибка конекта!")
    conn.close()
    return qwestion

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    global this_quiz
    global qwestion
    global db_data
    global COUNT
    random_answer = [1,2,3,4]
    random.shuffle(random_answer)
    COUNT = 0
    db_data = get_data_from_db(message.from_user.id)
    qwestion = get_qwestion_from_db(db_data[0])
    #os.system("echo "+str(message.chat.id)+" > test.txt") 
    this_quiz  = await bot.send_poll(message.chat.id, qwestion[0], [qwestion[random_answer[0]], qwestion[random_answer[1]], qwestion[random_answer[2]], qwestion[random_answer[3]]], type='quiz', correct_option_id=random_answer.index(1), is_anonymous=False)
    return this_quiz

@dp.poll_answer_handler()
async def handler_poll_answer(poll_answer: types.PollAnswer):
    # проверяем ответ
    #global this_quiz
    global COUNT
    if this_quiz.poll.correct_option_id == poll_answer.option_ids[0]:
        wright_result(poll_answer.user.id, 1, 'linux')
        await bot.send_message(poll_answer.user.id, 'Правильно! Идём дальше')
    else:
        wright_result(poll_answer.user.id, 0, 'linux')
        await bot.send_message(poll_answer.user.id, 'Жаль, но это неправильный ответ. Двигаемся дальше - может потом повезёт')
    if  COUNT == len(db_data):
        COUNT = 0
        await bot.send_message(poll_answer.user.id, 'Тет пройден, пасибо, брат.')

    else:
        COUNT = COUNT + 1
        try:
            qwestion = get_qwestion_from_db(db_data[COUNT])
        except IndexError:
            await bot.send_message(poll_answer.user.id, 'Тет пройден, пасибо, брат.\n Твой результат:')
    # генерируем списк дл перемешивания запроов
    random_answer = [1,2,3,4]
    random.shuffle(random_answer)
    # отправляем следующую викторину
    await bot.send_poll(poll_answer.user.id, qwestion[0], [qwestion[random_answer[0]], qwestion[random_answer[1]], qwestion[random_answer[2]], qwestion[random_answer[3]]], type='quiz', correct_option_id=random_answer.index(1), is_anonymous=False)
    #await bot.send_poll(poll_answer.user.id, len(db_data), [str(COUNT), "b", "c", "d"], type='quiz', correct_option_id=0, is_anonymous=False)
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
