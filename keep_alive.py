from flask import Flask
from threading import Thread

flask_app = Flask(__name__)


@flask_app.route('/health', methods=['GET'])
def healthcheck():
    return 'OK', 200


def run_flask_app():
    flask_app.run(host='0.0.0.0')


def keep_alive():
    flash_thread = Thread(target=run_flask_app)
    flash_thread.start()
