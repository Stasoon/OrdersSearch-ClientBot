from config import api_id, api_hash, client_app_name, sessions_folder_path, main_chat_id
from pyrogram import Client
from pyrogram.enums import ChatType
from pyrogram.types import Message
from os import path
from keep_alive import keep_alive


if __name__ == '__main__':
    keep_alive()


client_app = Client(f'{sessions_folder_path}/{client_app_name}', api_id, api_hash)
if not path.exists(f'{sessions_folder_path}/{client_app_name}.session'):
    client_app.start()
print('Бот запущен!')


def is_message_contain_keywords(message_text) -> bool:
    text = message_text.lower()
    is_about_design = (('веб-дизайн' not in text) and ('вебдизайн' not in text) and ('дизайн' in text)) or (
            'фотошоп' in text) or ('лого' in text) or ('ретушь' in text) or ('баннер' in text)
    is_about_prog = (('бот' in text) and ('работ' not in text))
    return is_about_prog or is_about_design


@client_app.on_message(group=True)
def handle_messages(client: Client, message: Message):
    try:
        if message.text is not None and message.chat.type == ChatType.SUPERGROUP:
            if is_message_contain_keywords(message.text):
                client.forward_messages(chat_id=main_chat_id, from_chat_id=message.chat.id, message_ids=message.id)
    except Exception as e:
        print(e)


try:
    client_app.run()
except Exception as e:
    print(e)
