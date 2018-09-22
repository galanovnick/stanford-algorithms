from utils.dataprovider import get
import itertools


raw = get(
    'https://d3c33hcgiwev3.cloudfront.net/_eed1bd08e2fa58bbe94b24c06a20dcdb_huffman.txt?Expires=1525737600&Signature='
    'NPw7hN-PhBq1TZDmGnyas-qRVK~a~7RF6R341n8v3xjqXY6sWSCjpQoob7mF4OK7L3QN~pBuCKIOcRhvAEwN38chAvAGJSruwtFEAjerrSxhUdbIs0'
    'iL0xR6n9ZsL1rzMMaREGY-WcGyv3nK7DIKqPF6tnKIm~4jcFqXbjGpxmM_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A'
).split("\n")

print([i != 0 for i in range(len(raw))])





