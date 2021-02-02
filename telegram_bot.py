from telegram import Bot
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters
from text_preparation import prepare_answer
from telegram import KeyboardButton
from telegram import ReplyKeyboardMarkup

from text_preparation import write_request

def make_start(bot, update):
	print("first message recieved")
	bot.send_message(chat_id=update.message.chat_id, text="Hello. My Name is ///a. I am robot AI. I was build to manage robot with a help of speech so you can find some mistakes in my request but they are all great if you'll try to pronounce them.",
		reply_markup=get_inline_keyboard())

def answer(bot, update):
	text = update.message.text.lower().replace(".", "").replace("?", "").replace("!", "").strip(" ")
	print("Request: " + str(text))
	answer = prepare_answer(text).lower()
	write_request(text, answer)
	ready_answer = ""
	answer = answer.split(". ")
	for sentence in answer:
		ready_answer += sentence.capitalize() + ". "
	ready_answer = ready_answer.replace("  ", " ").strip(" ")

	if text == "hey":
		ready_answer = "m?"

	if text.find("telegram") != -1:
		ready_answers = ['you know answer', 'i know that you know']

	print("Answer: " + str(ready_answer))
	bot.send_message(chat_id=update.message.chat_id, text=ready_answer, reply_markup=get_inline_keyboard())

def get_inline_keyboard():
	keyboard = [
			[
				KeyboardButton("Hey"),
				KeyboardButton("How are you"),
			],
			[
				KeyboardButton("Say something"),
				KeyboardButton("Weather"),
			],
                        [
                                KeyboardButton("How old are you"),
                                KeyboardButton("Let's play sea battle"),
                                KeyboardButton("Stop sea battle")
                   ],
                        [
                                KeyboardButton("What day of week is it today")
			],
			[
                                KeyboardButton("What day of month is it today"),
                        ],
			[
				KeyboardButton("When did you registered you telegram account"),
                        ],
			[
				KeyboardButton("Haven't hear you for a long time"),
                        ],
			[
				KeyboardButton("Let's play words"),
                        ],
			[
				KeyboardButton("Let's play words --debug"),
                        ],
			[
				KeyboardButton("Stop"),
                        ],
			[
				KeyboardButton("Delete this word"),
                        ],


	]
	return ReplyKeyboardMarkup(keyboard=keyboard)

def main():
	bot = Bot (token="1247626625:AAHl0mBgshQuehPirtKMjylpoGEDXlI0pGE", base_url="https://telegg.ru/orig/bot")
	updater = Updater(bot=bot)

	start_handler = CommandHandler("start", make_start)
	message_handler = MessageHandler(Filters.text, answer)

	updater.dispatcher.add_handler(start_handler)
	updater.dispatcher.add_handler(message_handler)

	updater.start_polling()
	updater.idle()

if __name__ == "__main__":
	print("start bot...")
	main()
