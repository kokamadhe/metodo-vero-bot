import os
from telegram import Bot

# Set your bot token and channel ID
TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = "@metodogold"
POST_FOLDER = "posts"
TRACK_FILE = "last_post.txt"

bot = Bot(token=TOKEN)

def get_next_post():
    try:
        with open(TRACK_FILE, "r") as f:
            last = int(f.read().strip())
    except:
        last = 0

    next_post = last + 1
    post_path = f"{POST_FOLDER}/post{next_post}.txt"

    if os.path.exists(post_path):
        with open(post_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Invia messaggio su Telegram
        bot.send_message(chat_id=CHANNEL_ID, text=content, parse_mode="Markdown")

        # Aggiorna file di tracking
        with open(TRACK_FILE, "w") as f:
            f.write(str(next_post))
    else:
        print("✅ Tutti i post sono già stati pubblicati.")

if __name__ == "__main__":
    get_next_post()

