"""
Write a Python program to execute a string containing Python code.
"""


code = """
def sum(x,y):
    return x+y

print('Sum of 203 and 303 is: ',sum(203,303))
"""

exec(code)
