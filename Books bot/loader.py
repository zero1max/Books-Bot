from aiogram import Dispatcher , Router, Bot
from aiogram.enums import ParseMode
from database.db_handlers import Database
from aiogram.client.default import DefaultBotProperties

db = Database()
dp = Dispatcher()
router = Router()
bot = Bot(token="YOUR_BOT_TOKEN", 
          default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp.include_router(router=router)