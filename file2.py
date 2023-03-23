from  file1 import Callme


# PS C:\dl\PBP\FlaskIntro> python .\file1.py
# Hello World
# __main__
# PS C:\dl\PBP\FlaskIntro> python .\file2.py
# Hello World
# file1
# Traceback (most recent call last):
#   File "C:\dl\PBP\FlaskIntro\file2.py", line 1, in <module>
#     from  file1 import Callme
# ImportError: cannot import name 'Callme' from 'file1' (C:\dl\PBP\FlaskIntro\file1.py)