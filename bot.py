from os import path
from pyrogram import Client
from pyrogram.enums import ChatType
from pyrogram.types import Message
from flask import Flask


# region FlaskApp
app = Flask(__name__)


@app.route('/', methods=['GET'])
def root():
    return 'Bot works!', 200


@app.route('/health', methods=['GET'])
def healthcheck():
    return 'OK', 200


def run_flask_app():
    app.run(host='0.0.0.0')


if __name__ == '__main__':
    run_flask_app()
# endregion


# region Pyrogram
api_id = 22134811
api_hash = '2f9b49ea388cfbaf99a55355c0238c08'
name = 'misha'

client = Client(f'session/{name}', api_id, api_hash)
if not path.exists(f'session/{name}.session'):
    client.start()
print('Бот запущен!')

main_chat_id = -1001830476676


@client.on_message(group=True)
def handle_messages(client: Client, message: Message):
    try:
        if message.text is not None and message.chat.type == ChatType.SUPERGROUP :
            text = message.text
            design = (('веб-дизайн' not in text) and ('вебдизайн' not in text) and ('дизайн' in text)) or (
                        'фотошоп' in text) or ('лого' in text) or ('ретушь' in text)
            prog = ('бот' in text and 'работ' not in text)
            if design or prog:
                client.forward_messages(chat_id=main_chat_id, from_chat_id=message.chat.id, message_ids=message.id)
    except Exception as e:
        print(e)


client.run()
# endregion
