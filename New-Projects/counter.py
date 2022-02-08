import time


def countdown(timer: int) -> None:
    while timer:
        mins, secs = divmod(timer, 60)
        timers = '{:02d}:{:02d}'.format(mins, secs)
        print(timers, end='\r')
        time.sleep(1)
        timer -= 1
    print('Timer completed!')


t = int(input('Enter the time of seconds: '))
countdown(t)
