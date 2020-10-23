import sys
import logging
import logging.config
from slackbot.bot import Bot
from slacker import Error
from slackbot import settings

def main():
  kw = {
      'format': '[%(asctime)s] %(message)s',
      'datefmt': '%m/%d/%Y %H:%M:%S',
      'level': logging.DEBUG,
      'stream': sys.stdout,
  }
  logging.basicConfig(**kw)
  logging.getLogger('requests.packages.urllib3.connectionpool').setLevel(logging.WARNING)

  try:
    bot = Bot()
    bot.run()
  except (Error) as e:
    print(f"{e}")

if __name__ == "__main__":
  print('start slackbot')
  main()
