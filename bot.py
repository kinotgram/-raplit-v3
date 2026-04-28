import re
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
import engine

TOKEN = "8763087192:AAFKXwlURObfuJlqhyz0sM7Uo66CZKjKD8c"

def is_youtube(url):
    return "youtube.com" in url or "youtu.be" in url

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if is_youtube(text):
        await update.message.reply_text("Video wird verarbeitet (V3)...")

        result = engine.process_video(text)

        await update.message.reply_text(
            f"Fertig!\n\nCaption:\n{result['caption']}\n\nHashtags:\n{result['hashtags']}"
        )
    else:
        await update.message.reply_text("Bitte YouTube Link senden")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot läuft V3...")
    app.run_polling()

if __name__ == "__main__":
    main()
