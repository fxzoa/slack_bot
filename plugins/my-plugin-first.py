from slackbot.bot import respond_to
from slackbot.bot import listen_to
from slackbot.bot import default_reply
import re
import json

config_json = "config.json"

@default_reply
def my_default_handler(message):
    message.reply('...')

@default_reply(matchstr=r'^default.*')
def default_handler(message):
    message.reply('***')

@respond_to('hi', re.IGNORECASE)
def hi(message):
    message.reply('I can understand hi or HI!')
    message.react('+1')

@respond_to('I love you')
def love(message):
    message.reply('I love you too!')

@listen_to('Can')
def help(message):
    # Message is replied to the sender (prefixed with @user)
    message.reply('Yes, I can!')

    # Message is sent on the channel
    message.send('I can help everybody!')

    # Start a thread on the original message
    message.reply("Here's a threaded reply", in_thread=True)

@respond_to(r'^list.*')
def list_func(message):
    with open(config_json, "r") as config_file:
        json_data = json.load(config_file)
        reply = json.dumps(json_data, indent=4)

    message.reply("```\n追加削除はこのファイルです ⇒ config_json\n{}```".format(reply))

@respond_to(r'^plan.*')
def plan_func(message):
    message.reply("ok! ちょっと待ってて!")