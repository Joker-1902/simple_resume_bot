# Простой Telegram-бот и FastAPI
## Установка
1. Активируйте ваше виртуальное окружение:
   
   - Windows PowerShell:
     ```powershell
     .venv\\Scripts\\Activate.ps1
     ```

2. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

   - Для разбора PDF нужен `PyPDF2`.
   - Для DOCX нужен `python-docx`.

3. Создайте `.env` по примеру:
   ```env
   BOT_TOKEN=ваш_токен_бота
   ```

## Запуск бота
```bash
python bot.py
```
Бот поддерживает:
- `/resume` — отправьте PDF/DOCX/TXT, бот вернёт текст.
- `/search` — пришлёт 3 заглушки вакансий с кнопками.

## Запуск FastAPI
```bash
uvicorn fastapi_app:app --reload
```
