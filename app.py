from flask import Flask
import logging

app = Flask(__name__)

logger = logging.getLogger('MyFlaskApp')
logger.setLevel(logging.INFO)
console_handler = logging.StreamHandler()
formatter = logging.Formatter('%(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

import routes

if __name__ == '__main__':
    logger.info('Starting Flask app')
    app.run(debug=True)