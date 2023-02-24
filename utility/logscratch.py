# uses a global variable to enable disable logging
# todo: perhaps use a singleton instead of global variable

enable_log_info = False


def info(data):
    if enable_log_info:
        print(data)
