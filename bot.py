from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler

async def start(update: Update, context):
    await update.message.reply_text("✅ Бот работает!")

def main():
    app = ApplicationBuilder().token("7881390086:AAHPfv0SvY1ljBOwMSzVQjryCVgzfPoI0Xk").build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if name == "__main__":
    main()