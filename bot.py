import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

# TOKEN hier einfügen
TOKEN = "8763087192:AAFKXwlURObfuJlqhyz0sM7Uo66CZKjKD8c"

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    await update.message.reply_text("Link erhalten. Verarbeitung startet...")

    print("Received:", text)

    # hier später Pipeline starten
    # engine.process_video(text)

    await update.message.reply_text("Fertig (Test Mode)")

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot läuft...")
    app.run_polling()

if __name__ == "__main__":
    main()
