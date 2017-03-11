import sys
import os

filename = 'NYSE_Close.csv'

lines = open(filename, 'r').readlines() 
del lines[-1] 
open(filename, 'w').writelines(lines) 