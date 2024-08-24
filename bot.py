import os 
import telebot
import time

#BOT_TOKEN is a variable in my linux machine, you can set it yourself
BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)



def message(chat_id, text):
    bot.send_message(chat_id, text)

def tail_f(file_path, interval=1.0):
    with open(file_path, 'r') as f:
        f.seek(0, 2)  
        while True:
            line = f.readline()
            if line:
                yield line
            else:
                time.sleep(interval)

if __name__ == "__main__":
    chat_id = ""
    path = "/var/log/auth.log"
    for new_line in tail_f(path):
        message(chat_id, new_line)
