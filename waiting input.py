import time
import _thread


def print_t( name, delay ):
    while 1:
        time.sleep(delay)
        print(name)


_thread.start_new_thread(print_t("first", 1,))
_thread.start_new_thread(print_t("second", 2,))

