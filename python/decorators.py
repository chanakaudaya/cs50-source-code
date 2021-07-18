def announce(f):
    def wrapper():
        print("Before function")
        f()
        print("After function")
    return wrapper

@announce
def hello():
    print("Hello world")

hello()