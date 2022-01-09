import signal

def my_sig_handler(signum, frame):
    print("")

signal.signal(signal.SIGALRM, my_sig_handler)

while True:
    signal.alarm(1)
    print(":)")
    signal.pause()
