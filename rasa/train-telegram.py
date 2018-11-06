import logging
import os
import train

from rasa_core import utils
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.agent import Agent
from rasa_core.channels import HttpInputChannel
from rasa_core.channels.telegram import TelegramInput


logger = logging.getLogger(__name__)

# If you want to use your own bot to development add the bot credentials as
# second parameters
TELEGRAM_ACCESS_TOKEN = os.getenv('TELEGRAM_ACCESS_TOKEN', '')
VERIFY = os.getenv('VERIFY', '')
WEBHOOK_URL = os.getenv('WEBHOOK_URL', '')


def run():
    interpreter = RasaNLUInterpreter('models/nlu/default/current')

    agent = Agent.load('models/dialogue', interpreter=interpreter)

    input_channel = TelegramInput(
        access_token=TELEGRAM_ACCESS_TOKEN,
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
