from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

admin = ReplyKeyboardMarkup(
    resize_keyboard=True,
    #one_time_keyboard=True,
    keyboard=[
        [KeyboardButton(text='Kitob yuklash💾')]
    ]
)

tekwrw_del_book = ReplyKeyboardMarkup(
    one_time_keyboard=True,
    resize_keyboard=True,
    keyboard=[
        [KeyboardButton(text="Kitob o'chirish🗑"), KeyboardButton(text="Ortga qaytish🔙")]
    ]
)

delete_book = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder='Tanlang...',
    keyboard=[
        [KeyboardButton(text="1 ta kitobni o'chirish"), KeyboardButton(text="Barcha kitobni o'chirish")]
    ]
)

del50 = ReplyKeyboardMarkup(
    one_time_keyboard=True,
    resize_keyboard=True,
    input_field_placeholder="Tanlang...",
    keyboard=[
        [KeyboardButton(text="Ha"), KeyboardButton(text="Yo'q")]
    ]
)

del100 = ReplyKeyboardMarkup(
    one_time_keyboard=True,
    resize_keyboard=True,
    input_field_placeholder="Tanlang...",
    keyboard=[
        [KeyboardButton(text="Ha 100%"), KeyboardButton(text="Yo'q")]
    ]
)


classes = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder='Sinfingizni tanlang...',
    keyboard=[
        [KeyboardButton(text='5-sinf'), KeyboardButton(text='6-sinf'), KeyboardButton(text='7-sinf')],
        [KeyboardButton(text='8-sinf'), KeyboardButton(text='9-sinf'), KeyboardButton(text='10-sinf')],
        [KeyboardButton(text='11-sinf')]
    ]
)


books_5 = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Kitobni tanlang...",
    keyboard=[
        [KeyboardButton(text='📘Adabiyot 5'),KeyboardButton(text='📕Matematika 5'),KeyboardButton(text='📗Geografiya 5')],
        [KeyboardButton(text='📒Ingliz tili 5'),KeyboardButton(text='📕Tarbiya 5'),KeyboardButton(text='📗Tarix 5')],
        [KeyboardButton(text='📘Ona tili 5'),KeyboardButton(text='📒Biologiya 5'),KeyboardButton(text='📗Rus tili 5')],
        [KeyboardButton(text='Asosiy menu🏠')]
    ]
)

books_6 = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Kitobni tanlang...",
    keyboard=[
        [KeyboardButton(text='📘Adabiyot 6')],
        [KeyboardButton(text='📕Matematika 6')],
        [KeyboardButton(text='📗Geografiya 6')],
        [KeyboardButton(text='📒Ingliz tili 6')],
        [KeyboardButton(text='📕Tarbiya 6')],
        [KeyboardButton(text='📗Tarix 6')],
        [KeyboardButton(text='📘Ona tili 6')],
        [KeyboardButton(text='📒Biologiya 6')],
        [KeyboardButton(text='📗Rus tili 6')],
        [KeyboardButton(text='Asosiy menu🏠')]
    ]
)

books_7 = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Kitobni tanlang...",
    keyboard=[
        [KeyboardButton(text='📘Adabiyot 7')],
        [KeyboardButton(text='📕Matematika 7')],
        [KeyboardButton(text='📗Geografiya 7')],
        [KeyboardButton(text='📒Ingliz tili 7')],
        [KeyboardButton(text='📕Tarbiya 7')],
        [KeyboardButton(text='📗Tarix 7')], 
        [KeyboardButton(text='📘Ona tili 7')],
        [KeyboardButton(text='📒Biologiya 7')],
        [KeyboardButton(text='📗Rus tili 7')],
        [KeyboardButton(text='📕Fizika 7')],
        [KeyboardButton(text='Asosiy menu🏠')]
    ]
)

books_8 = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Kitobni tanlang...",
    keyboard=[
        [KeyboardButton(text='📘Adabiyot 8')],
        [KeyboardButton(text='📕Matematika 8')],
        [KeyboardButton(text='📗Geografiya 8')],
        [KeyboardButton(text='📒Ingliz tili 8')],
        [KeyboardButton(text='📕Tarbiya 8')],
        [KeyboardButton(text='📗Tarix 8')],
        [KeyboardButton(text='📘Ona tili 8')],
        [KeyboardButton(text='📒Biologiya 8')],
        [KeyboardButton(text='📗Rus tili 8')],
        [KeyboardButton(text='📕Fizika 8')],
        [KeyboardButton(text='Asosiy menu🏠')]
    ]
)

books_9 = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Kitobni tanlang...",
    keyboard=[
        [KeyboardButton(text='📘Adabiyot 9')],
        [KeyboardButton(text='📕Matematika 9')],
        [KeyboardButton(text='📗Geografiya 9')],
        [KeyboardButton(text='📒Ingliz tili 9')],
        [KeyboardButton(text='📕Tarbiya 9')],
        [KeyboardButton(text='📗Tarix 9')],
        [KeyboardButton(text='📘Ona tili 9')],
        [KeyboardButton(text='📒Biologiya 9')],
        [KeyboardButton(text='📗Rus tili 9')],
        [KeyboardButton(text='📘Python 9')],
        [KeyboardButton(text='📕Fizika 9')],
        [KeyboardButton(text='Asosiy menu🏠')]
    ]
)

books_10 = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Kitobni tanlang...",
    keyboard=[
        [KeyboardButton(text='📘Adabiyot 10')],
        [KeyboardButton(text='📕Matematika 10')],
        [KeyboardButton(text='📗Geografiya 10')],
        [KeyboardButton(text='📒Ingliz tili 10')],
        [KeyboardButton(text='📕Tarbiya 10')],
        [KeyboardButton(text='📗Tarix 10')],
        [KeyboardButton(text='📘Ona tili 10')],
        [KeyboardButton(text='📒Biologiya 10')],
        [KeyboardButton(text='📗Rus tili 10')],
        [KeyboardButton(text='📕Fizika 10')],
        [KeyboardButton(text='Asosiy menu🏠')]
    ]
)

books_11 = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Kitobni tanlang...",
    keyboard=[
        [KeyboardButton(text='📘Adabiyot 11')],
        [KeyboardButton(text='📕Matematika 11')],
        [KeyboardButton(text='📗Geografiya 11')],
        [KeyboardButton(text='📒Ingliz tili 11')],
        [KeyboardButton(text='📕Tarbiya 11')],
        [KeyboardButton(text='📗Tarix 11')],
        [KeyboardButton(text='📘Ona tili 11')],
        [KeyboardButton(text='📒Biologiya 11')],
        [KeyboardButton(text='📗Rus tili 11')],
        [KeyboardButton(text='📕Fizika 11')],
        [KeyboardButton(text='Asosiy menu🏠')]
    ]
)