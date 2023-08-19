import random
import schedule
import datetime
import time
import telegram
from telegram.ext import Updater, CallbackContext

TOKEN = '6636021133:AAHsK0RlwiUQew-IHFfYt8eIgDAMj4Y-QPU'

def enviar_mensagem(context: CallbackContext):
    chat_id = -1001868373788
    emojis = ['💣'] * 25

    diamantes = 4  # Alterado para 4 diamantes
    for _ in range(diamantes):
        while True:
            index = random.randint(0, len(emojis) - 1)
            if emojis[index] == '💣':
                emojis[index] = '💎'
                break

    grade = '\n'.join([' '.join(emojis[i:i + 5]) for i in range(0, len(emojis), 5)])

    horario_atual = datetime.datetime.now()
    horario_validade = horario_atual + datetime.timedelta(minutes=random.randint(0, 0) + 3)
    horario_validade_str = horario_validade.strftime('%H:%M')

    mensagem = (
        f"O sistema gerou os seguintes:\n\n{grade}\n\n"
        f"Aposte com: 3 💣.\n"
        f"🎯 Use até 2 gales\n"
        f"⏰ Validade até às {horario_validade_str}\n"
        f"🎯 PLATAFORMA: https://betslots.bet/y4c8kxc0r"
    )

    context.bot.send_message(chat_id=chat_id, text=mensagem)

def main():
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    job_minute = updater.job_queue.run_repeating(enviar_mensagem, interval=10, first=0)

    updater.start_polling()

    updater.idle()

if __name__ == "__main__":
    main()
