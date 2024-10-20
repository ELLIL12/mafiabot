import telebot
import random

bot = telebot.TeleBot('7883139018:AAGaMHDoRfVT6K2V7FaGQwETVxrRlP2Wu2M')
user_dict = {}

# Словарь для хранения зарегистрированных пользователей и их кодов игр
registered_users = {0: {'group': 'haha', 'id': []}, 1: {'group': 'Проверка 2', 'id': [1195384026], 'name': 'Ponyo'}}
# роли игроков
roles = []

# первое взаимодействие с ботом
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет, я бот для игры в мафию! Используйте команду /register, чтобы зарегистрироваться для игры.")


# промежуточный этап запроса кода игры
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
        # блокировка добавлений новых участников, исключение из списка повторяющиеся id, проверка достаточности количества участников
        for game_code in registered_users:
            if registered_users[game_code]['group'] == message.chat.title:
                if len(set(registered_users[game_code]['id'])) > 0:
                    registered_users[game_code]['id'] = set(registered_users[game_code]['id'])
                    send_private_messages(message.chat.title)
                else:
                    bot.send_message(message.chat.id,
                                     f'У вас недостаточное количество игроков, игра будет неинтересной(. '
                                     f'Минимальное количество: '
                                     f'5, текущее количество: {len(set(registered_users[game_code]["id"]))}')



    if 'начать игру' in message.text.lower():
        # Получаем имя бота
        bot_username = bot.get_me().username

        # Создаем ссылку
        bot_link = f"https://t.me/{bot_username}"

        # Создаем встроенную клавиатуру
        markup = telebot.types.InlineKeyboardMarkup()
        button = telebot.types.InlineKeyboardButton("Перейти к боту", url=bot_link)
        markup.add(button)
        # добавляем в словарь с регистрацией название группы и ее номер
        group_title = message.chat.title
        registered_users[max(registered_users) + 1] = {'group': group_title}
        registered_users[max(registered_users)]['id'] = []

        # Отправляем сообщение с клавиатурой
        bot.send_message(message.chat.id, f"Привет всем! Я - бот для игры в мафию. Уникальный кот вашей игры - {max(registered_users)}. "
                              f"\n Все пользователи, желающие сыграть, напишите мне в личные сообщения команду \register"
                                          f"\n Когда все желающие играть, будут зарегестрированы, напишите: играть, и мы начнем игру",
                         reply_markup=markup)


# отправка личных сообщений с ролью
def send_private_messages(chat_title):
    for game_code in registered_users:
        if registered_users[game_code]['group'] == chat_title:
            try:
                # вызов класса и присвоение ролей игрокам
                player_role = roles(registered_users[game_code]['id'])
                registered_users[game_code]['id'] = player_role.role_for_all()

                for user_id in registered_users[game_code]['id']:
                    if registered_users[game_code]['id'][user_id] == 'liberal':
                        markup = telebot.types.InlineKeyboardMarkup()
                        button1 = telebot.types.InlineKeyboardButton("либерал",
                                                                     callback_data="либерал")
                        markup.add(button1)
                        # Отправляем сообщение с кнопками
                        bot.send_message(user_id, "Привет! Твоя роль: либерал", reply_markup=markup)
                    elif registered_users[game_code]['id'][user_id] == 'fashist':
                        markup = telebot.types.InlineKeyboardMarkup()
                        button1 = telebot.types.InlineKeyboardButton("фашистик",
                                                                     callback_data="фашистик")
                        markup.add(button1)
                        # Отправляем сообщение с кнопками
                        bot.send_message(user_id, "Привет! Твоя роль: фашистик", reply_markup=markup)
                    elif registered_users[game_code]['id'][user_id] == 'gitler':
                        markup = telebot.types.InlineKeyboardMarkup()
                        button1 = telebot.types.InlineKeyboardButton("гитлер",
                                                                     callback_data="гитлер")
                        markup.add(button1)
                        # Отправляем сообщение с кнопками
                        bot.send_message(user_id, "Привет! Твоя роль: гитлер", reply_markup=markup)
            except Exception as e:
                print(f"Ошибка при отправке сообщения пользователю {user_id}: {e}")


# вызов описания персонажа, следует написать описания всех персонажей
@bot.callback_query_handler(func=lambda call: call.data == "фашистик")
def callback_greet(call):
    bot.answer_callback_query(
        call.id,
        text='Ты тут злой', show_alert=True)


@bot.callback_query_handler(func=lambda call: call.data == "либерал")
def callback_greet(call):
    bot.answer_callback_query(
        call.id,
        text='Борешься зо злом', show_alert=True)


@bot.callback_query_handler(func=lambda call: call.data == "гитлер")
def callback_greet(call):
    bot.answer_callback_query(
        call.id,
        text='Ты тут вообще самый злой', show_alert=True)

def main():
    bot.polling(none_stop=True)


class roles:
    def __init__(self, sps):
        self.count_of_membres = len(sps)
        self.players = list(sps)
        print(sps)
        self.players_roles = {}
        self.roles = []

    def roles_from_count(self):
        if self.count_of_membres == 5:
            self.roles = ['liberal', 'liberal', 'liberal', 'fashist', 'hitler']
        elif self.count_of_membres == 6:
            self.roles = ['liberal', 'liberal', 'liberal', 'liberal', 'fashist', 'hitler']
        elif self.count_of_membres == 7:
            self.roles = ['liberal', 'liberal', 'liberal', 'liberal', 'fashist', 'fashist', 'hitler']
        elif self.count_of_membres == 8:
            self.roles = ['liberal', 'liberal', 'liberal', 'liberal', 'liberal', 'fashist', 'fashist', 'hitler']
        elif self.count_of_membres == 9:
            self.roles = ['liberal', 'liberal', 'liberal', 'liberal', 'liberal', 'fashist', 'fashist', 'fashist', 'hitler']
        elif self.count_of_membres == 10:
            self.roles = ['liberal', 'liberal', 'liberal', 'liberal', 'liberal', 'liberal', 'fashist', 'fashist', 'fashist',
                          'hitler']
        # test
        elif self.count_of_membres == 2:
            self.roles = ['fashist', 'liberal']
        return self.roles

    def role_for_all(self):
        self.roles = self.roles_from_count()
        random.shuffle(self.roles)
        for i in range(self.count_of_membres):
            self.players_roles[self.players[i]] = self.roles[i]
        return self.players_roles


if __name__ == "__main__":
    main()