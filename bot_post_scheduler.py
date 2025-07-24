import time
import telebot

# Inserisci qui il token del tuo bot Telegram
BOT_TOKEN = "7767035120:AAH5E7wLW5KmRa5q-fJSXEap0vDle8mBvsI"

# Inserisci qui l'username del canale (con @) oppure l'ID numerico (es. -1001234567890)
CHANNEL_ID = "@metodogold"

# Lista dei post da pubblicare (testo semplice)
posts = [
    "💡 **3 modi semplici per iniziare a guadagnare online oggi**\n\n"
    "1️⃣ Iscriviti a programmi di affiliazione (Amazon, Binance, ecc.)\n"
    "2️⃣ Usa app di cashback e sondaggi retribuiti\n"
    "3️⃣ Crea contenuti su social e monetizza (YouTube, TikTok, Instagram)\n\n"
    "📌 Segui il canale per approfondire ogni metodo nei prossimi post!",

    "⚠️ **Mai investire senza sapere cosa stai facendo!**\n\n"
    "Molti perdono soldi perché partono senza conoscenze.\n"
    "Prima di investire, studia, prova metodi demo, fai domande.\n\n"
    "🧠 Ricorda: il guadagno serio nasce dalla preparazione, non dalla fortuna.",

    "🛠️ **App gratuita per tracciare i tuoi guadagni**\n\n"
    "Consiglio di usare “Money Manager” (disponibile su Android e iOS) per tenere sotto controllo entrate e uscite.\n\n"
    "📊 Conoscere bene le tue finanze è il primo passo per crescere.",

    "🎯 **Come Luca ha iniziato con 0€ e ora guadagna extra**\n\n"
    "Luca ha iniziato seguendo semplici consigli di affiliazione.\n"
    "Ha dedicato 30 minuti al giorno per creare contenuti e condividere link.\n"
    "Ora ha un guadagno extra mensile di 200€-300€.\n\n"
    "💪 Anche tu puoi farcela, basta costanza!",

    "❓ **Qual è la tua esperienza con il guadagno online?**\n\n"
    "Scrivi nei commenti o rispondi qui:\n"
    "➡️ Hai già provato qualche metodo?\n"
    "➡️ Quale ti piacerebbe approfondire?\n"
    "➡️ Qual è la tua più grande difficoltà?\n\n"
    "🤝 Condividere aiuta a crescere insieme!"
]

def main():
    bot = telebot.TeleBot(BOT_TOKEN)

    for post in posts:
        try:
            bot.send_message(CHANNEL_ID, post, parse_mode="Markdown")
            print(f"Post inviato con successo:\n{post}\n")
        except Exception as e:
            print(f"Errore nell'invio del post: {e}")

        # Aspetta 2 ore (7200 secondi) prima del prossimo post
        time.sleep(7200)

if __name__ == "__main__":
    main()
