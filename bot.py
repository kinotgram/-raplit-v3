import re
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
import engine

# ⚠️ HIER DEIN NEUER TOKEN EINTRAGEN
TOKEN = "8763087192:AAFKXwlURObfuJlqhyz0sM7Uo66CZKjKD8c"

def is_youtube(url):
    return "youtube.com" in url or "youtu.be" in url

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    print("DEBUG: MESSAGE RECEIVED:", text)

    if is_youtube(text):
        await update.message.reply_text("Video wird verarbeitet...")

        print("DEBUG: CALLING ENGINE")

        result = engine.process_video(text)

        print("DEBUG: ENGINE RETURNED:", result)

        await update.message.reply_text(
            f"Fertig!\n\nCaption:\n{result['caption']}\n\nHashtags:\n{result['hashtags']}"
        )

    else:
        await update.message.reply_text("Bitte YouTube Link senden")

        except Exception as e:
            await update.message.reply_text(f"❌ Fehler in Engine:\n{str(e)}")
            print("ENGINE ERROR:", e)

    else:
        await update.message.reply_text("❗ Bitte sende einen YouTube Link")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("🤖 Bot läuft V3...")
    app.run_polling()

if __name__ == "__main__":
    main()
