from urllib import request
from heapq import heappush, heappop, heapify

class Node:
	minBytes = None
	maxBytes = None

	def __init__(self, minBytes = 0, maxBytes = 0):
		self.minBytes = minBytes
		self.maxBytes = maxBytes

srcUrl = ("https://d3c33hcgiwev3.cloudfront.net/_eed1bd08e2fa58bbe94b24c06a20dcdb_huffman.txt"
	"?Expires=1526601600&Signature=GkcH0~D7Zx3-MiyDPy~vY2puhVDWCdf6Fq6pOVdGfFJcylOPXr20l"
	"Vp9vKcgNuqcLQoHEpn3Q0nP6CTiIeiOJmtWK0OjOWmr5ap--jHT90baD~U9ZM2Bozqe54Jyl0FJUONcTyHBi"
	"NaD8RDKZAKjPWeb~ReYNoGL1v0TEV4BhKM_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A");
raw = request.urlopen(srcUrl).read().decode("utf-8")

weights = raw.split("\n")
del weights[0]
del weights[len(weights) - 1]
weights = list(map(lambda item: (int(item), Node()), weights))
heap = []

for x in weights:
	heappush(heap, x)

min1 = None
min2 = None
while len(heap) > 1:
	min1 = heappop(heap)
	min2 = heappop(heap)
	new = Node(min(min1[1].minBytes, min2[1].minBytes) + 1, max(min1[1].maxBytes, min2[1].maxBytes) + 1)
	heappush(heap, (min1[0] + min2[0], new))

result = heappop(heap)[1]
print(result.minBytes)
print(result.maxBytes)

