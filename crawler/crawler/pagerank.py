import numpy
import json
from pprint import pprint

with open("test/result.json") as f:
  data = json.load(f)

pprint(data)

size = len(data)
print(size)

prematrix = [[]] * size
keys = list(data.keys())
print(keys)

for i in range(size):
  print(i)
  print(keys[i])
  prematrix[i] = [1/len(data[keys[i]]) if (keys[j] in data[keys[i]]) else 0 for j in range(size)]

matrix = numpy.matrix(prematrix)
pprint(matrix)