#!/usr/bin/python3
# 5-no_c.py
def no_c(my_string):
   esp = ""
   for i in range(len(my_string)):
       if (my_string[i] != 'c' and my_string[i] != 'C'):
           esp += my_string[i]
           return esp
