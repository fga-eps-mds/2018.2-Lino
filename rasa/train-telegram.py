import logging
import os
import train

from rasa_core import utils
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.agent import Agent
from rasa_core.interpreter import RegexInterpreter
from rasa_core.channels import HttpInputChannel
from rasa_core.channels.telegram import TelegramInput


logger = logging.getLogger(__name__)

# If you want to use your own bot to development add the bot credentials as
# second parameters
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN', '625051845:AAGFkfemDjiriY4uRdIR7ayujxLdzwileLg')
VERIFY = os.getenv('VERIFY', 'lininhofga_bot')
WEBHOOK_URL = os.getenv('WEBHOOK_URL', 'https://d4a3b020.ngrok.io/webhook')


def run():
    interpreter = RasaNLUInterpreter('models/nlu/default/current')
    agent = Agent.load('models/dialogue', interpreter=interpreter)

    input_channel = TelegramInput(
        access_token=ACCESS_TOKEN,
        verify=VERIFY,
        webhook_url=WEBHOOK_URL
    )

    agent.handle_channel(HttpInputChannel(5002, "", input_channel))


if __name__ == '__main__':
    utils.configure_colored_logging(loglevel='DEBUG')

    logger.info("Train NLU")
    train.train_nlu()
    logger.info("Train Dialogue")
    train.train_dialogue()
    logger.info("Run")
    run()
