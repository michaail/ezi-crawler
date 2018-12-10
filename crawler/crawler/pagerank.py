import numpy
import json
from pprint import pprint

with open("test/result.json") as f:
  data = json.load(f)

pprint(data)

size = len(data)

prematrix = [[]] * size
keys = list(data.keys())
print(keys)

for i in range(size):
  print(keys[i])
  prematrix[i] = [1/len(data[keys[i]]) if (keys[j] in data[keys[i]]) else 0 for j in range(size)]

matrix = numpy.matrix(prematrix)
pprint(matrix)

# pprint(matrix[0])
count = size
alpha = 0.15

def page_pageRank(ppr, itr):
  
  pr_array = []
  for i in range(count):
    row = numpy.squeeze(numpy.asarray(matrix[:,i]))
    suma = 0
    # print(row)
    for j in range(len(row)):
      # print(row[j])
      suma += ppr[j]*row[j]
    page_rank = alpha + (1 - alpha)*suma
    pr_array.append(page_rank)
  
  itr += 1
  if itr == 50:
    return(pr_array)
  else:
    return page_pageRank(pr_array, itr)

PR = page_pageRank([1,1,1,1,1], 0)

dictionary = dict(zip(keys, PR))
for key, value in dictionary.items():
  print(key + " - " + str(value))