LEXICON: dict[str, str] = {

    'start': '<b>Привет, {name}!</b>\n'
               'Рад видеть Вас в своем магазине 😊',
    'help_info': 'Информация заполняется администратором 🕸',
    'faq_info': 'Информация заполняется администратором 🕸',
    'other_answer': 'Хммм, похоже я не понимаю, что вы от меня хотите.\n'
                    'Попробуйте воспользоваться командой \n '
                    '/help',
    'catalog': '🗃 Каталог',
    'catalog_not_exist': 'Каталог пока пуст, заходите попозже 🕸',
    'basket': '🛒 Корзина',
    'replenish_balance': '💰 Пополнить баланс',
    'admin': 'Здравствуйте, Администратор, чего желаете? ☣',
    'not_admin': 'К сожалению, у вас нет прав для входа в меню администратора ❗',
    'admin_menu_placeholder': 'Выберите из возможных вариантов:',
    'no_category': 'Категории еще не созданы, введите название категории для создания ❕',
    'no_products': 'К сожалению, в этой категории пока нет товаров, зайдите позже 🆘',
    'choice_category': 'Выберите категорию, куда хотите добавить товар ❕',
    'download_category': '🗄 Добавить категорию',
    'download_category_1': 'Введите название категории ❕',
    'exists_category': 'Такая категория уже существует, попробуйте ввести другое название ‼',
    'no_exists_category': 'Пока не существует ни одной категории',
    'successful_name_cat': 'Добавление категории прошло успешно ✅',
    'not_successful_name_cat': 'Похоже, такая категория уже существует, '
                               'попробуйте создать новую или удалить имеющуюся ❗',
    'delete_category': '❌ Удалить категорию',
    'delete_category_1': 'Выберите категорию для удаления ❕',
    'delete_category_2': 'Или нажмите "Отмена" для возврата в меню Администратора',
    'delete_category_3': 'Категория была удалена успешно ✅',
    'download_product': '🆕 Загрузить товары',
    'delete_product': '❌ Удалить товары',
    'delete_product_1': 'Категории с товарами:',
    'delete_product_2': '❌ Удалить товар',
    'successful_deleted_product': 'Товар был успешно удален ✅',
    'back_to_main_menu_button': '⬅ В главное меню',
    'text_name_category': 'Или введите название новой категории',
    'main_menu': 'Вы в главном меню!',
    'cancel_fsm_button': 'Отмена',
    'show_basket': '<b>Ваша корзина:</b>\n\n'
                   '{products}\n\n'
                   '{length} \n'
                   'Общая стоимость заказа:\n\n'
                   '<b>{total_price} ₽ </b> \n',
    'profile': '💼 Профиль',
    'user': '<b>Это ваш профиль, {name}!</b>\n\n'
            '💰 Ваш баланс: {balance} ₽\n\n'
            '📅 Дата регистрации: {reg_date} \n\n'
            '🧾 Количество покупок: {buy_counter} \n\n'
            '🤝 Количество приглашенных друзей: {ref_counter} \n\n'
            '🔗 Ваша реферальная ссылка: \n{ref_link} \n\n',
    'FSM_download_1': 'Пожалуйста, загрузите фото 🖼',
    'FSM_cancel': 'Хорошо, процесс был отменен 👌',
    'not_photo': 'Это не похоже на фото, давайте еще разок ❗',
    'FSM_photo_sent': 'Отлично, теперь отправьте мне название товара ✅',
    'incorrect_name': 'Похоже вы ввели некорректное имя товара, попробуйте еще раз ❗',
    'FSM_descr_sent': 'Отправьте, пожалуйста, описание товара ✅',
    'incorrect_descr': 'Описание должно состоять только из букв и цифр, попробуйте еще раз ❗',
    'FSM_price_sent': 'Напишите цену товара в рублях 💲',
    'incorrect_price': 'Цена должна быть цифрой и больше нуля ❗',
    'FSM_finish': 'Поздравляю!\n'
                  'Товар загружен ♻',
    'backward': '⏪',
    'forward': '⏩',
    'back_to_catalog': '⬅ Назад к каталогу',
    'back': '⬅ Назад',
    'add_to_basket': 'Добавить в корзину 🧾',
    'add_button': 'Вы добавили товар в корзину ✅',
    'pay': '💳 Оплатить',
    'edit_basket': '❌ Редактировать',
    'msg_for_edit_basket': 'Выберите товар, который хотите удалить',
    'deleted_product_basket': 'Товар удален из вашей корзины ✅',
    'empty_basket': 'Ваша корзина пуста 🕸',
    'download_catalog_photo': '🖼 Загрузить фото каталога',
    'photo_for_catalog': 'Отправьте мне фото для каталога ❕',
    'unsuccessful_photo': 'Похоже вы отправили мне не фото, попробуйте еще раз ❗',
    'amount_money_for_replenish': 'Введите сумму на которую хотите увеличить баланс ❕',
    'user_not_exist': 'Такого пользователя не существует ❗\n'
                      'Попробуйте еще раз!',
    'unsuccessful_id_for_balance': 'Telegram ID должен быть числом ❗',
    'unsuccessful_amount_for_balance': 'Сумма пополнения должна быть числом и больше нуля ❗',
    'successful_replenish_balance': 'Баланс успешно пополнен ✅',
    'product_settings': '🧰 Управление товарами',
    'statistics': '📊 Статистика',
    'general_settings': '⚙ Общие настройки бота',
    'back_to_admin_menu_button': '⬅ Назад к меню Администратора',
    'back_to_admin_menu': 'Вы вернулись в меню Администратора ❕',
    'FAQ_button': '🗺 FAQ',
    'edit_help': '✏ Редактировать help',
    'edit_faq': '✏ Редактировать FAQ',
    'text_for_help': 'Введите текст для кнопки help 📥',
    'text_for_faq': 'Введите информация для вкладки FAQ 📥',
    'successful': 'Все прошло успешно! ✅',
    'suc_ref_link': 'По вашей реферальной ссылке, кто то успешно зарегистрировался ❕',
    'suc_reg_link': 'Вы успешно зарегистрировались по чужой реферальной ссылке ✅',
    'own_ref_link': 'Регистрация по собственной реферальной ссылке не возможна ❗',
    'repeated_ref_link': 'Повторная регистрация по чужой реферальной ссылке не возможна ❗',
    'accept_payment': 'Вы уверены, что хотите оплатить данную покупку ❔',
    'yes': '✅ Да',
    'no': '❌ Нет',
    'successful_payment': 'Покупка была успешно оплачена ✅',
    'not_enough_money': 'Недостаточно денежных средств на балансе ❗',
    'statistics_info': '📊 <b> Статистика бота: </b> \n\n'
                       '👤 Количество пользователей: <b>{users}</b>\n\n'
                       '💰 Общая сумма балансов пользователей: <b>{users_balance}</b> ₽ \n\n'
                       '🤝 Количество реферальных пользователей: <b>{ref_users}</b>\n\n'
                       '🧾 Общее количество покупок: <b>{total_buys}</b>'

}