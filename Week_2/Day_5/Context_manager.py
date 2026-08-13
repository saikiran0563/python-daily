# from contextlib import contextmanager

# @contextmanager
# def my_context():
#     print("Start")
#     yield
#     print("End")


# with my_context():
#     print("Inside")


class MyContext():
    def __enter__(self):
        print("Entering Context")

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting Context")

with MyContext():
    print("Inside context")
    x= 10/0
