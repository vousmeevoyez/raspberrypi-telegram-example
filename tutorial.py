""" 
    Raspberry Pi with press button connected to Telegram examples
"""
import os
import json
import telebot
import RPi.GPIO as GPIO

class TeleButton:

    button_pin = 3

    def __init__(self):
        # SETUP GPIO HERE
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(self.button_pin, GPIO.RISING, callback=self.greet_user)

        # SETUP TELEGRAM BOT HERE
        self._bot = telebot.TeleBot(os.environ.get("TELEGRAM_TOKEN"))

    def greet_user(self, channel):
        """greet user here """
        print("button was pressed")
        self._bot.send_message("742457643", "Hello!")

    def start(self):
        # start pooling here
        self._bot.polling()
        # start user input here
        while True:
            user_input = raw_input("Enter quit to exit ")
            if user_input == "quit":
                GPIO.cleanup()
                break

if __name__ == "__main__":
    TeleButton().start()
