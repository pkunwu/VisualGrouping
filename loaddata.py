#load a csv file (~200Mb).
import numpy as np

filepath = input('Enter the absolute file path:')

with open(filepath, 'r') as f:
    for line in f:
        pass