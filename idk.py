# выбор канцлера президентом

    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    # проверка
    if len(dict_of_group['och']) == 1:
        print(str(dict_of_group['och'][0]))
        but1 = telebot.types.InlineKeyboardButton(dict_of_group['names'][dict_of_group['och'][0]], callback_data='id' + str(dict_of_group['och'][0]))
        # Добавляем кнопки в клавиатуру
        markup.add(but1)

    elif len(dict_of_group['och']) == 5:
        but1 = telebot.types.InlineKeyboardButton(dict_of_group['names'][str(dict_of_group['och'][1])], 'id' + str(dict_of_group['och'][1]))
        but2 = telebot.types.InlineKeyboardButton(dict_of_group['names'][str(dict_of_group['och'][2])], 'id' + str(dict_of_group['och'][2]))
        but3 = telebot.types.InlineKeyboardButton(dict_of_group['names'][str(dict_of_group['och'][3])], 'id' + str(dict_of_group['och'][3]))
        but4 = telebot.types.InlineKeyboardButton(dict_of_group['names'][str(dict_of_group['och'][4])], 'id' + str(dict_of_group['och'][4]))

        # Добавляем кнопки в клавиатуру
        markup.add(but1, but2, but3, but4)

    elif len(dict_of_group['och']) == 6:
        but1 = telebot.types.InlineKeyboardButton(dict_of_group['names'][str(dict_of_group['och'][1])], 'id' + str(dict_of_group['och'][1]))
        but2 = telebot.types.InlineKeyboardButton(dict_of_group['names'][str(dict_of_group['och'][2])], 'id' + str(dict_of_group['och'][2]))
        but3 = telebot.types.InlineKeyboardButton(dict_of_group['names'][str(dict_of_group['och'][3])], 'id' + str(dict_of_group['och'][3]))
        but4 = telebot.types.InlineKeyboardButton(dict_of_group['names'][str(dict_of_group['och'][4])], 'id' + str(dict_of_group['och'][4]))
        but5 = telebot.types.InlineKeyboardButton(dict_of_group['names'][str(dict_of_group['och'][5])],
                                                  'id' + str(dict_of_group['och'][5]))

        # Добавляем кнопки в клавиатуру
        markup.add(but1, but2, but3, but4, but5)

    elif len(dict_of_group['och']) == 7:
        but1 = telebot.types.InlineKeyboardButton(dict_of_group['names'][str(dict_of_group['och'][1])], 'id' + str(dict_of_group['och'][1]))
        but2 = telebot.types.InlineKeyboardButton(dict_of_group['names'][str(dict_of_group['och'][2])], 'id' + str(dict_of_group['och'][2]))
        but3 = telebot.types.InlineKeyboardButton(dict_of_group['names'][str(dict_of_group['och'][3])], 'id' + str(dict_of_group['och'][3]))
        but4 = telebot.types.InlineKeyboardButton(dict_of_group['names'][str(dict_of_group['och'][4])], 'id' + str(dict_of_group['och'][4]))
        but5 = telebot.types.InlineKeyboardButton(dict_of_group['names'][str(dict_of_group['och'][5])],
                                                  'id' + str(dict_of_group['och'][5]))
        but6 = telebot.types.InlineKeyboardButton(dict_of_group['names'][str(dict_of_group['och'][6])],
                                                  'id' + str(dict_of_group['och'][6]))

        # Добавляем кнопки в клавиатуру
        markup.add(but1, but2, but3, but4, but5, but6)

    elif len(dict_of_group['och']) == 8:
        but1 = telebot.types.InlineKeyboardButton(dict_of_group['names'][str(dict_of_group['och'][1])], 'id' + str(dict_of_group['och'][1]))
        but2 = telebot.types.InlineKeyboardButton(dict_of_group['names'][str(dict_of_group['och'][2])], 'id' + str(dict_of_group['och'][2]))
        but3 = telebot.types.InlineKeyboardButton(dict_of_group['names'][str(dict_of_group['och'][3])], 'id' + str(dict_of_group['och'][3]))
        but4 = telebot.types.InlineKeyboardButton(dict_of_group['names'][str(dict_of_group['och'][4])], 'id' + str(dict_of_group['och'][4]))
        but5 = telebot.types.InlineKeyboardButton(dict_of_group['names'][str(dict_of_group['och'][5])],
                                                  'id' + str(dict_of_group['och'][5]))
        but6 = telebot.types.InlineKeyboardButton(dict_of_group['names'][str(dict_of_group['och'][6])],
                                                  'id' + str(dict_of_group['och'][6]))
        but7 = telebot.types.InlineKeyboardButton(dict_of_group['names'][str(dict_of_group['och'][7])],
                                                  'id' + str(dict_of_group['och'][7]))

        # Добавляем кнопки в клавиатуру
        markup.add(but1, but2, but3, but4, but5, but6, but7)

    elif len(dict_of_group['och']) == 9:
        but1 = telebot.types.InlineKeyboardButton(dict_of_group['names'][str(dict_of_group['och'][1])], 'id' + str(dict_of_group['och'][1]))
        but2 = telebot.types.InlineKeyboardButton(dict_of_group['names'][str(dict_of_group['och'][2])], 'id' + str(dict_of_group['och'][2]))
        but3 = telebot.types.InlineKeyboardButton(dict_of_group['names'][str(dict_of_group['och'][3])], 'id' + str(dict_of_group['och'][3]))
        but4 = telebot.types.InlineKeyboardButton(dict_of_group['names'][str(dict_of_group['och'][4])], 'id' + str(dict_of_group['och'][4]))
        but5 = telebot.types.InlineKeyboardButton(dict_of_group['names'][str(dict_of_group['och'][5])],
                                                  'id' + str(dict_of_group['och'][5]))
        but6 = telebot.types.InlineKeyboardButton(dict_of_group['names'][str(dict_of_group['och'][6])],
                                                  'id' + str(dict_of_group['och'][6]))
        but7 = telebot.types.InlineKeyboardButton(dict_of_group['names'][str(dict_of_group['och'][7])],
                                                  'id' + str(dict_of_group['och'][7]))
        but8 = telebot.types.InlineKeyboardButton(dict_of_group['names'][str(dict_of_group['och'][8])],
                                                  'id' + str(dict_of_group['och'][8]))

        # Добавляем кнопки в клавиатуру
        markup.add(but1, but2, but3, but4, but5, but6, but7, but8)

    elif len(dict_of_group['och']) == 10:
        but1 = telebot.types.InlineKeyboardButton(dict_of_group['names'][str(dict_of_group['och'][1])], 'id' + str(dict_of_group['och'][1]))
        but2 = telebot.types.InlineKeyboardButton(dict_of_group['names'][str(dict_of_group['och'][2])], 'id' + str(dict_of_group['och'][2]))
        but3 = telebot.types.InlineKeyboardButton(dict_of_group['names'][str(dict_of_group['och'][3])], 'id' + str(dict_of_group['och'][3]))
        but4 = telebot.types.InlineKeyboardButton(dict_of_group['names'][str(dict_of_group['och'][4])], 'id' + str(dict_of_group['och'][4]))
        but5 = telebot.types.InlineKeyboardButton(dict_of_group['names'][str(dict_of_group['och'][5])],
                                                  'id' + str(dict_of_group['och'][5]))
        but6 = telebot.types.InlineKeyboardButton(dict_of_group['names'][str(dict_of_group['och'][6])],
                                                  'id' + str(dict_of_group['och'][6]))
        but7 = telebot.types.InlineKeyboardButton(dict_of_group['names'][str(dict_of_group['och'][7])],
                                                  'id' + str(dict_of_group['och'][7]))
        but8 = telebot.types.InlineKeyboardButton(dict_of_group['names'][str(dict_of_group['och'][8])],
                                                  'id' + str(dict_of_group['och'][8]))
        but9 = telebot.types.InlineKeyboardButton(dict_of_group['names'][str(dict_of_group['och'][9])],
                                                  'id' + str(dict_of_group['och'][9]))


        # Добавляем кнопки в клавиатуру
        markup.add(but1, but2, but3, but4, but5, but6, but7, but8, but9)