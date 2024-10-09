import telebot

bot = telebot.TeleBot('7883139018:AAGaMHDoRfVT6K2V7FaGQwETVxrRlP2Wu2M')
user_dict = {}

# Словарь для хранения зарегистрированных пользователей и их кодов игр
registered_users = {0: {'group': 'haha', 'id': []}, 1: {'group': 'Проверка 2', 'id': [1195384026], 'name': 'Ponyo'}}
#роли игроков
roles = []

#первое взаимодействие с ботом
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет, я бот для игры в мафию! Используйте команду /register, чтобы зарегистрироваться для игры.")


#промежуточный этап запроса кода игры
@bot.message_handler(commands=['register'])
def register_user(message):
    msg = bot.reply_to(message, "Пожалуйста, введите номер игры для регистрации:")
    bot.register_next_step_handler(msg, process_game_code)


def process_game_code(message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    game_code = message.text

    try:
        registered_users[int(game_code)]['id'].append(user_id)
        registered_users[int(game_code)]['name'] = user_name
        # Сохраняем пользователя и код игры в словаре
        bot.reply_to(message, f"{user_name}, вы успешно зарегистрированы на игру в группе {registered_users[int(game_code)]['group']}!")
    except Exception as e:
        bot.reply_to(message, f"{user_name}, такого номера игры не существует!")

    print(registered_users)



@bot.message_handler(func=lambda message: True)
def check_message(message):
    if 'играем' in message.text.lower():
        send_private_messages(message.chat.title)

    if 'начать игру' in message.text.lower():
        # Получаем имя бота
        bot_username = bot.get_me().username

        # Создаем ссылку
        bot_link = f"https://t.me/{bot_username}"

        # Создаем встроенную клавиатуру
        markup = telebot.types.InlineKeyboardMarkup()
        button = telebot.types.InlineKeyboardButton("Перейти к боту", url=bot_link)
        markup.add(button)
        #добавляем в словарь с регистрацией название группы и ее номер
        group_title = message.chat.title
        registered_users[max(registered_users) + 1] = {'group': group_title}
        registered_users[max(registered_users)]['id'] = []

        # Отправляем сообщение с клавиатурой
        bot.send_message(message.chat.id, f"Привет всем! Я - бот для игры в мафию. Уникальный кот вашей игры - {max(registered_users)}. "
                              f"Все пользователи, желающие сыграть, напишите мне в личные сообщения команду \start",
                         reply_markup=markup)


# отправка личных сообщений с ролью
def send_private_messages(chat_title):
    for game_code in registered_users:
        if registered_users[game_code]['group'] == chat_title:
            try:
                for user_id in registered_users[game_code]['id']:
                    bot.send_message(user_id, f'Привет! Твоя роль: ?')
            except Exception as e:
                print(f"Ошибка при отправке сообщения пользователю {user_id}: {e}")


def main():
    bot.polling(none_stop=True)


if __name__ == "__main__":
    main()