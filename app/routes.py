from app import app
from flask import request
from telebot.types import Update
from bot import bot
url='/'+API_KEY
@app.route(url,methods=['POST'])
def handle(request):
    if request.method=="POST":
        json_string=request.get_data().decode('utf-8')
        update=Update.de_json(json_string)
        bot.process_new_update(update)
