from threading import

def display():
    for i in range(1,11):
        print("Display",i)

t = Thread(traget = display)
t.start()

