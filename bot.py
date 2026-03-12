from telegram import Update
from telegram.ext import ApplicationBuilder,MessageHandler, filters, ContextTypes

TOKEN = "8682800667:AAEpig_1D8alwQT_9o9lhp0xJ9qCS0kRuYM"

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message:
        user_message = update.message.text
        await update.message.reply_text(f"You said: {user_message}")
        await update.message.reply_text("what next?")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT,reply))

app.run_polling()