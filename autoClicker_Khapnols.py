import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode


print("""

░░╔╗╔═╦╗░░░░░░░░░░░░░╔╗░░░░░
░░║║║╔╣║░░░░░░░░░░░░░║║░░░░░
░░║╚╝╝║╚═╦══╦══╦═╗╔══╣║╔══╗░
░░║╔╗║║╔╗║╔╗║╔╗║╔╗╣╔╗║║║══╣░
░░║║║╚╣║║║╔╗║╚╝║║║║╚╝║╚╬══║░
░░╚╝╚═╩╝╚╩╝╚╣╔═╩╝╚╩══╩═╩══╝░
░░░░░░░░░░░░║║░░░░░░░░░░░░░░
""")
time.sleep(3)

#text area
print("Programı başlatmak için 'S' tuşuna basınız. / Press the 'S' key to start the program.")
print("Programdan çıkış yapmak için 'E' tuşuna basınız / Press the 'E' key to exit the program.")
time.sleep(2)

#tıklama süresi / click time 
delay = 3
t = 2
#basılacak tuş / key to press
button = Button.left
#programı çalıştıran tuş /key to run the program
start_stop_key = KeyCode(char='s')
#programı kapatan tuş / key to exit the program
exit_key = KeyCode(char='e')
print('=====================================================================================================')
print('Program Başladı S Tuşu İle Çalıştırabilirsin / The program has started, you can run it with the S key')
print('=====================================================================================================')

class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True
    def start_clicking(self):
        time.sleep(t)
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                mouse.click(self.button)
                time.sleep(self.delay)
            time.sleep(0.1)


mouse = Controller()
click_thread = ClickMouse(delay, button)
click_thread.start()


def on_press(key):
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()
    elif key == exit_key:
        click_thread.exit()
        listener.stop()


with Listener(on_press=on_press) as listener:
    listener.join()