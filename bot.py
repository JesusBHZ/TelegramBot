from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters
import os

token = "6035437090:AAGBpKI74hI64gZhDal3TX_IYNBhhhS7yCA"

def start(bot,update):
    try:
        user_data = update.message.from_user
        update.message.reply_text("Hola estoy listo")
        print(f"{user_data}")
    except Exception as e:
        print(f"Error start:{e.args}")

def help(bot,update):
    try:
        update.message.reply_text(f"Este bot tiene los siguientes comandos... \n /operaciones ")
    except Exception as e:
        print(f"Error help:{e.args}")

def echo(bot,update):
    try:
        text = update.message.text
        update.message.reply_text(f"{text}")
    except Exception as e:
        print(f"Error echo:{e.args}")

def operaciones(bot,update):
    try:
        text = update.message.text
        print(text)
        if text == "/operaciones":
            update.message.reply_text(f"OPERACIONES")
            text = update.message.text
            if '+' in text:
                text = update.message.text.split('+')
                numero1 = text[0]
                numero2 = text[1]
                suma = int(numero1) + int(numero2)
                update.message.reply_text(f"{suma}")
            elif '*' in text:
                text = update.message.text.split('*')
                numero1 = text[0]
                numero2 = text[1]
                suma = int(numero1) * int(numero2)
                update.message.reply_text(f"{suma}")
            elif '/' in text:
                text = update.message.text.split('/')
                numero1 = text[0]
                numero2 = text[1]
                suma = int(numero1) / int(numero2)
                update.message.reply_text(f"{suma}")
            elif '-' in text:
                text = update.message.text.split('-')
                numero1 = text[0]
                numero2 = text[1]
                suma = int(numero1) - int(numero2)
                update.message.reply_text(f"{suma}")
        else:
            update.message.reply_text(f"{text}")
    except Exception as e:
        print(f"Error echo:{e.args}")

def error(bot,update,error):
    try:
        print(f"Update {update} genero el error {error}")
    except Exception as e:
        print(f"Error en error: {e.args}")

def image(bot, update):
    try:
        print("Recibiendo imagen")
        user_data = update.message.from_user
        print(user_data)
        file = bot.getFile(update.message.photo[-1].file_id)
        filename = os.path.join('downloads/images/', 'imagen.jpg')
        file.download(filename)
        update.message.reply_text(f"Imagen recibida")
    except Exception as e:
        print(f"Error image: {e.args}")

def main():
    try:
        print("YisusBot iniciando el token")
        updater = Updater(token)

        print("YisusBot iniciando dispacher")
        db = updater.dispatcher

        print("YisusBot iniciando commandHandler")
        db.add_handler(CommandHandler("start",start)),
        db.add_handler(CommandHandler("help",help))
        #db.add_handler(CommandHandler(Filters.text,operaciones))
        #db.add_handler(CommandHandler("operaciones", operaciones()))
        db.add_handler(MessageHandler(Filters.photo,image))
        db.add_handler(MessageHandler(Filters.text,echo))

        db.add_error_handler(error)

        updater.start_polling()

        print("YisusBot iniciando el bot")
        updater.idle()
    
    except Exception as e:
        print(f"Error main: {e.args}")

if  __name__ == "__main__":
    main()