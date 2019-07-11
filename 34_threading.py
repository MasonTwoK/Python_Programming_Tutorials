import threading

class ChillyMessenger(threading.Thread):
    def run(self):
        for _ in range(100000):
            print(threading.currentThread().getName())

x = ChillyMessenger(name="Send out messages")
y = ChillyMessenger(name="Recive messages")
x.start()
y.start()


