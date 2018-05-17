from urllib import request

class Node:
	w = 0
	temp = 0

	def __init__(self, weight):
		self.w = int(weight)

srcUrl = ("https://d3c33hcgiwev3.cloudfront.net/_790eb8b186eefb5b63d0bf38b5096873_mwis.txt?"
	"Expires=1526601600&Signature=dJ1aNFi4DhvPfgU9R4kF-6QXPxEk4ZQ-qpExcfS6FSZ5gtemNcjyYE7FM"
	"HsQwF5ff6agBM9EsusNhwgfQ5f7TACDf34aLXbhAREZZV48cKjcngPTfN9MAexjThUMY9vEV5IbRdpCXKkNw4bY"
	"R4MK5JO3MeiT0JmzHkaGjKNMeWY_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A");
raw = request.urlopen(srcUrl).read().decode("utf-8")

# 1, 2, 3, 4, 17, 117, 517, 997
indicies = [0, 1, 2, 3, 16, 116, 516, 996]

weights = raw.split("\n")
weights.pop(0)
weights.pop()
weights = list(map(Node, weights))
amount = len(weights)

def left(arr, i):
	return arr[i].w + (arr[i - 2].temp if i > 1 else 0)
def right(arr, i):
	return arr[i - 1].temp if i > 0 else 0

for i in range(0, amount):
	weights[i].temp = max(left(weights, i), right(weights, i))

result = [None] * amount

i = amount - 1
while i > -1:
	result[i] = left(weights, i) > right(weights, i)
	i -= 2 if result[i] else 1

for i in range(0, amount):
	if i > 0 and result[i-1] == result[i]:
		print('dang')

print([result[i] for i in indicies])

#01010000
#00100110