from django.test import TestCase
import pickle


# Create your tests here.
# dev_28 시리얼라이제이션의 이해
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.area = width * height

def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2


class objectAPItest(TestCase):
    def setUp(self):
        pass

    def test_path(self):

        dict = {
            "add":add,
            "sub":sub,
        }
        url = "add"
        print(dict[url](1,2))
        url = "sub"
        print(dict[url](1,2))

    def test_serialization(self):
        rect = Rectangle(10, 20)

        with open("rect.data", "wb") as f:
            pickle.dump(rect, f)

        with open("rect.data", "rb") as f:
            r = pickle.load(f)

        print(r.width, r.height)
