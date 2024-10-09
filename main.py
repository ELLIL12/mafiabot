import telebot


bot = telebot.TeleBot('7883139018:AAGaMHDoRfVT6K2V7FaGQwETVxrRlP2Wu2M')
user_dict = {}

# Словарь для хранения зарегистрированных пользователей и их кодов игр
registered_users = {}


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

    # Сохраняем пользователя и код игры в словаре
    registered_users[user_id] = {'name': user_name, 'game_code': game_code}

    bot.reply_to(message, f"{user_name}, вы успешно зарегистрированы на игру с номером: {game_code}!")


@bot.message_handler(func=lambda message: True)
def check_message(message):
    if 'играем' in message.text.lower():
        send_private_messages()


#отправка личных сообщений с ролью
def send_private_messages():
    for user_id, user_info in registered_users.items():
        user_name = user_info['name']
        try:
            bot.send_message(user_id, f'Привет, {user_name}! Твоя роль?')
        except Exception as e:
            print(f"Ошибка при отправке сообщения пользователю {user_id}: {e}")


def main():
    bot.polling(none_stop=True)


if __name__ == "__main__":
    main()