def my_decorator(func):
    def wrapper():
        print("Task started")
        func()
        print("Task ended")
    return wrapper()
