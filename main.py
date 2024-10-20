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
                if len(set(registered_users[game_code]['id'])) > 4:
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
                for user_id in registered_users[game_code]['id']:
                    markup = telebot.types.InlineKeyboardMarkup()
                    button1 = telebot.types.InlineKeyboardButton("мирный житель",
                                                                 callback_data="мирный житель")
                    markup.add(button1)

                    # Отправляем сообщение с кнопками
                    bot.send_message(user_id, "Привет! Твоя роль: ?", reply_markup=markup)
            except Exception as e:
                print(f"Ошибка при отправке сообщения пользователю {user_id}: {e}")


# вызов описания персонажа, следует написать описания всех персонажей
@bot.callback_query_handler(func=lambda call: call.data == "мирный житель")
def callback_greet(call):
    bot.answer_callback_query(
        call.id,
        text='Ты - мирный житель. Твоя задача вычислить мафию и убедить всех избавиться от преступника днем', show_alert=True)


#Класс карточек законов
class Cards:
    def __init__(self):
        self.cards_in = ["fascist"] * 11 +  ["liberal"] * 6 #карты в колоде
        self.cards_out = [] #сюда надо складывать карты которые откинули игроки

    
    #выкладка закона на стол
    def card_on_board(self):
        if len(self.cards_in) < 3:
            self.cards_in = self.cards_out + self.cards_in
            self.cards_out = []
        card = random.choice(self.cards_in), # Рандомно выбираем первую карту
        cards.remove(card)  # Удаляем 1 карту из списка карт в колоде
        card = [card] +  [random.choice(self.cards_in)] # Рандомно выбираем вторую карту закидываем обе карты в общий список
        cards.remove(card[1]) #Удаляем 2 карту из списка
        card = card + [random.choice(self.cards_in)]# Рандомно выбираем третью карту закидываем три карты в общий список
        cards.remove(card[2])  # Удаляем 3 карту из списка
        return card


class CardsOnBoard:
    #два списка: либеральные карты на столе, фашистские карты на столе
    def __init__(self):
        self.onboard_liberal = []
        self.onboard_fascist = []

    def move(self, cards):
        player_choose = cards.card_on_board
        #сюда добавить что выбирает игрок что откидывает, что откидывается идет в cards.cards_out
        #остальное идет президенту тоже самое происходит с выбором президента
        if chosen_card == "liberal":
            self.onboard_liberal.append(chosen_card)
        else:
            self.onboard_fascist.append(chosen_card)

def main():
    bot.polling(none_stop=True)


if __name__ == "__main__":
    main()
