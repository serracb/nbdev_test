# AUTOGENERATED! DO NOT EDIT! File to edit: 00_core.ipynb (unless otherwise specified).

__all__ = ['say_hello', 'multiply', 'read_image', 'read_image2', 'say_goodbye']

# Cell
def say_hello(to):
    "Say hello to somebody"
    return f'Hello {to}!'

# Cell
def multiply(a, b):
    "Multiplies a and b"
    return a*b

# Cell
from PIL import Image
def read_image(path):
    "Reads the image in path and return a PIL Image object"
    return Image.open(path)

# Cell
def read_image2(path):
    "Same as [`read_image`](/core#read_image) but implemented for doing some testing"
    return Image.open(path)

# Comes from 01_export_test.ipynb, cell
def say_goodbye(name):
    return("goodbye "+name)