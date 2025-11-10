# tests/test_hello.py

import sys
import os
sys.path.append(r"C:\Devops\PythonCI\hello-pipeline")

from hello import greet

def test_greet_default():
    assert greet() == "Hello, World!"

def test_greet_custom():
    assert greet("Madhu") == "Hello, Madhu!"
