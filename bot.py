from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
import engine

TOKEN = "8763087192:AAFKXwlURObfuJlqhyz0sM7Uo66CZKjKD8c"

def is_youtube(url: str):
    return "youtube.com" in url or "youtu.be" in url

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    print("📩 MESSAGE RECEIVED:", text)

    if not text:
        return

    if is_youtube(text):
        await update.message.reply_text("🎬 Video wird verarbeitet...")

        try:
            print("⚙️ ENGINE START")

            result = engine.process_video(text)

            print("✅ ENGINE DONE")

            await update.message.reply_text(
                "✅ Fertig!\n\n"
                f"📝 Caption:\n{result['caption']}\n\n"
                f"🏷 Hashtags:\n{result['hashtags']}"
            )

        except Exception as e:
            print("❌ ENGINE ERROR:", e)
            await update.message.reply_text(f"❌ Fehler:\n{str(e)}")

    else:
        await update.message.reply_text("❗ Bitte sende einen YouTube Link")

def main():
    print("🚀 BOT STARTING...")

    app = ApplicationBuilder().token(TOKEN).build()

    print("🚀 BOT BUILT")

    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)
    )

    print("🚀 HANDLER READY")

    app.run_polling()

if __name__ == "__main__":
    main()
