import os
from telegram import Bot

TOKEN = os.getenv("BOT_TOKEN")  # deve essere settata su Render come variabile d'ambiente
CHANNEL_ID = "@metodogold"
POSTS_FOLDER = "posts"
TRACK_FILE = "last_post.txt"

bot = Bot(token=TOKEN)

def send_next_post():
    # Leggi l'indice dell'ultimo post inviato
    try:
        with open(TRACK_FILE, "r") as f:
            last_post_num = int(f.read().strip())
    except FileNotFoundError:
        last_post_num = 0  # se non esiste, comincia da 0

    next_post_num = last_post_num + 1
    post_file = os.path.join(POSTS_FOLDER, f"post{next_post_num}.txt")

    if os.path.exists(post_file):
        with open(post_file, "r", encoding="utf-8") as f:
            content = f.read()

        # Invia il post al canale Telegram
        bot.send_message(chat_id=CHANNEL_ID, text=content, parse_mode="Markdown")

        # Aggiorna il file tracker
        with open(TRACK_FILE, "w") as f:
            f.write(str(next_post_num))

        print(f"Post {next_post_num} inviato con successo!")
    else:
        print("🎉 Hai già inviato tutti i post disponibili!")

if __name__ == "__main__":
    send_next_post()


