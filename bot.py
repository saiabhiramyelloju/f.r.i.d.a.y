import os
from telegram import Update
from telegram.ext import ApplicationBuilder,MessageHandler, filters, ContextTypes
from intent import process_message

TOKEN = os.getenv("BOT_TOKEN")
if TOKEN is None:
    raise ValueError("BOT_TOKEN environment variable not set")
async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message:
        user_message = update.message.text
        response = process_message(user_message)
        await update.message.reply_text(response)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT,reply))

app.run_polling()