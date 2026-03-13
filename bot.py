import os
from telegram import Update
from telegram.ext import ApplicationBuilder,MessageHandler, CommandHandler,filters, ContextTypes
from intent import process_message

TOKEN = os.getenv("BOT_TOKEN")
if TOKEN is None:
    raise ValueError("BOT_TOKEN environment variable not set")
async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message

    if message is None or message.from_user is None or message.text is None:
        return

    user_id = message.from_user.id
    user_message = message.text

    response = process_message(user_id, user_message)
    await message.reply_text(response)

app = ApplicationBuilder().token(TOKEN).build()
# command handler
app.add_handler(CommandHandler("start", reply))
app.add_handler(CommandHandler("add", reply))
app.add_handler(CommandHandler("subtract", reply))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND,reply))

app.run_polling()