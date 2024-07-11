from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram import F
from loader import router, bot, db
from keyboards.defoult.keybords import *
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
import time

class Book(StatesGroup):
    book_name = State()
    book_id = State()

class DeleteBook(StatesGroup):
    bookname = State()

class DeleteBooks(StatesGroup):
    bookname = State()

#ADMIN = 5471452269

#------------------------------------------Commands----------------------------------------------
@router.message(CommandStart())
async def start(msg: Message):
    await msg.answer_sticker('CAACAgIAAxkBAAICMWXS4nBhgkN3XNeZ05MjKHy0r4hRAAKaDAAC753ZS6lNRCGaKqt5NAQ')
    await msg.answer(f"Assalomu aleykum {msg.from_user.full_name}!")
    db.create_table()
    if msg.from_user.id == 5460739298 or msg.from_user.id == 5471452269:
        await msg.answer('Siz adminisiz!', reply_markup=admin)
    else:
        await msg.answer("Sinfingizni tanlang: ", reply_markup=classes)

@router.message(Command('id'))
async def id(msg: Message):
    await msg.answer(f'Sizning ID: <b>{msg.from_user.id}</b>')

@router.message(Command('books'))
async def books(msg: Message):
    book_info = db.select_books()
    for book in book_info:
        time.sleep(0.2)
        await msg.answer(f"1. id: {book[0]}\n2. book_name: {book[2]}\n3. book_id: {book[1]}")

@router.message(Command("help"))
async def yordam(msg: Message):
    await msg.answer(f"Savollaringiz bo'lsa <b>@zero1max</b> ga murojat qiling")

#----------------------------------------Downloads Books---------------------------------------
@router.message(F.text == 'Kitob yuklash💾')
async def book_set(msg: Message, state: FSMContext):
    await state.set_state(Book.book_name)
    await msg.answer("Kitob nomini yuboring✍️")

@router.message(Book.book_name)
async def bookname_set(msg: Message, state: FSMContext):
    await state.update_data(book_name=msg.text)
    await state.set_state(Book.book_id)
    await msg.answer("Kitob yuboring📨")

@router.message(Book.book_id, F.document)
async def bookid_set(msg: Message, state: FSMContext):
    document_id = msg.document.file_id
    await state.update_data(book_id= document_id)
    data = await state.get_data()
    bookname= data.get('book_name')
    bookid = data.get('book_id')
    await state.clear()
    db.add_books(book_id=bookid, book_name=bookname)
    await msg.answer("Kitob muvaffaqiyatli yuklandi✅")


#-----------------------------------------Delete Book--------------------------------
@router.message(F.text == "deletebookadmin")
async def tekwrw_delete_book(msg: Message):
    await msg.delete()
    await msg.answer("Ortga yo'l bo'lmasligi mumkin!", reply_markup=tekwrw_del_book)

@router.message(F.text == "Ortga qaytish🔙")
async def ortga(msg: Message):
    await msg.answer("Siz adminsiz!", reply_markup=admin)

@router.message(F.text == "Kitob o'chirish🗑")
async def deletebook(msg: Message, state: FSMContext):
      await msg.answer("Iltimos avval yaxshilab o'ylab ko'ring!!!")
      await msg.answer('Tanlang👇', reply_markup=delete_book)

#-------------------One Book Delete--------------------------
@router.message(F.text == "1 ta kitobni o'chirish")
async def one_book_delete(msg: Message, state: FSMContext):
    await state.set_state(DeleteBook.bookname)
    await msg.answer("Kitob nomini yuboring✍️")

@router.message(DeleteBook.bookname)
async def bookname_set(msg: Message, state: FSMContext):
    await state.update_data(bookname=msg.text)
    data = await state.get_data()
    booname= data.get('bookname')
    await state.clear()
    db.delete_one(value=booname)
    await msg.answer("Kitob o'chirildi✅")

#--------------------Delete Books-----------------------------
@router.message(F.text == "Barcha kitobni o'chirish")
async def del_books(msg: Message):
    await msg.answer("Rostan ham barcha kitoblarni o'chirib yubormoqchimisiz?", reply_markup=del50)

@router.message(F.text == 'Ha')
async def yes50(msg: Message, state: FSMContext):
    await msg.answer("Ishonchingiz komilmi?", reply_markup=del100)

@router.message(F.text == "Ha 100%")
async def yes100(msg: Message):
    db.delete_all()
    await msg.answer("Barcha kitoblar o'chirib yuborildi!\nTekshirish uchun /books ni bosing!")

@router.message(F.text == "Yo'q")
async def no(msg: Message):
    await msg.answer('Siz adminsiz!',reply_markup=admin)

#-----------------------------------------USER PANEL--------------------------------------------
@router.message(lambda msg: msg.text in  ['5-sinf', '6-sinf', '7-sinf', '8-sinf', '9-sinf', '10-sinf', '11-sinf'])
async def handle_buttons(msg: Message):
    if msg.text == '5-sinf':
        await msg.answer(f"Sizga {msg.text} kitoblaridan qaysi biri kerak\nTanlang:👇🏻", reply_markup=books_5)
    elif msg.text == '6-sinf':
        await msg.answer(f"Sizga {msg.text} kitoblaridan qaysi biri kerak\nTanlang:👇🏻", reply_markup=books_6)
    elif msg.text == '7-sinf':
        await msg.answer(f"Sizga {msg.text} kitoblaridan qaysi biri kerak\nTanlang:👇🏻", reply_markup=books_7)
    elif msg.text == '8-sinf':
        await msg.answer(f"Sizga {msg.text} kitoblaridan qaysi biri kerak\nTanlang:👇🏻", reply_markup=books_8)
    elif msg.text == '9-sinf':
        await msg.answer(f"Sizga {msg.text} kitoblaridan qaysi biri kerak\nTanlang:👇🏻", reply_markup=books_9)
    elif msg.text == '10-sinf':
        await msg.answer(f"Sizga {msg.text} kitoblaridan qaysi biri kerak\nTanlang:👇🏻", reply_markup=books_10)
    elif msg.text == '11-sinf':
        await msg.answer(f"Sizga {msg.text} kitoblaridan qaysi biri kerak\nTanlang:👇🏻", reply_markup=books_11)

#----------------------------------Ortga--------------------------
        
@router.message(F.text == 'Asosiy menu🏠')
async def ortga(msg: Message):
    await msg.answer('Asosiy menu🏠', reply_markup=classes)

#-------------------------------------Send books------------------------

@router.message(F.text)
async def get_book(msg: Message):
    user_id = msg.from_user.id
    bokname= msg.text
    book_info = db.select_book(bokname)
    if book_info:
        book_name = book_info[2]
        book_sticker = book_info[1]
        await bot.send_document(user_id, book_sticker)
        await bot.send_message(user_id, f"Bu kitobni yuklab oling: {book_name}")
    else:
        await msg.answer("Ushbu ID bo'yicha kitob topilmadi. Iltimos, to'g'ri ID kiriting.")

 
#---------------------------------------Nothing------------------------------------
@router.message()
async def nothing(msg: Message):
    await msg.answer("Chunmadim?")
    