# bot.py
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import docx
from PyPDF2 import PdfReader
import os
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# --- Обработка команды /start ---
@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Привет! \nИспользуй /resume чтобы отправить резюме или /search чтобы увидеть вакансии.")

# --- Команда /resume ---
@dp.message(Command("resume"))
async def resume_request(message: types.Message):
    await message.answer("Отправь мне PDF или DOCX файл с резюме.")

@dp.message(lambda m: m.document)
async def handle_resume(message: types.Message):
    doc = message.document
    if not (doc.file_name.endswith(".pdf") or doc.file_name.endswith(".docx")):
        await message.answer("Пожалуйста, отправь PDF или DOCX файл.")
        return

    file = await bot.download(doc)
    text = ""

    if doc.file_name.endswith(".pdf"):
        reader = PdfReader(file)
        for page in reader.pages:
            text += page.extract_text() or ""
    else:
        document = docx.Document(file)
        for para in document.paragraphs:
            text += para.text + "\n"

    await message.answer("📄 Текст из резюме:\n\n" + text[:3000])  # Telegram ограничивает длину сообщений

# --- Команда /search ---
@dp.message(Command("search"))
async def search(message: types.Message):
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=[
        [types.InlineKeyboardButton(text="Вакансия 1", url="https://example.com")],
        [types.InlineKeyboardButton(text="Вакансия 2", url="https://example.com")],
        [types.InlineKeyboardButton(text="Вакансия 3", url="https://example.com")],
    ])
    await message.answer("Вот несколько вакансий 🔍", reply_markup=keyboard)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
