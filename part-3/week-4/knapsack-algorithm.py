from utils.dataprovider import get
import time


def parse(data):
    lines = data.split('\n')
    lines.pop(-1)
    meta = lines.pop(0)
    return [
        int(meta.split(' ')[0]),
        list(map((lambda item: {"value": int(item.split(' ')[0]), "weight": int(item.split(' ')[1])}), lines))
    ]


def compute_optimal_knapsack_value(capacity, items):
    min_weight = min(items, key=lambda item: item['weight'])['weight']
    amount = len(items)
    matrix = [[0 for i in range(0, capacity)] for j in range(0, 2)]

    for i in range(1, amount):
        iter_time = time.time()

        weight = items[i]['weight']
        value = items[i]['value']

        for j in range(min_weight, capacity):
            value1 = matrix[0][j]
            value2 = matrix[0][j - weight] + value if j - weight > -1 else value
            matrix[1][j] = max(value1, value2)

        matrix[0] = matrix[1].copy()

        unit = time.time() - iter_time
        print("\n--- Iteration №%d took %f seconds ---" % (i, unit))
        print("--- Estimated time left: %f minutes ---" % ((amount - i + 1) * unit / 60))

    return matrix[1][capacity - 1]


start_time = time.time()

raw = get('https://d3c33hcgiwev3.cloudfront.net/_6dfda29c18c77fd14511ba8964c2e265_knapsack_big.txt?Expires=1'
          '537747200&Signature=X00go7sESB~efQUSw-rfMP6KQdnXaQqM3ctuRcXkD~eAwhDLm-3lW9T8ScgudaMbaMwCH9J5joy8B'
          'ATE8XXO5-C5MSpXRvKrDq9dnw6P~VkXr~8ReiW~JwaBpdCGsKmzCaWQhTVIuXix226RrcV-Vq1K6F4NF1EFnf3JOMqe5lY_'
          '&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A')

# raw = get('https://d3c33hcgiwev3.cloudfront.net/_6dfda29c18c77fd14511ba8964c2e265_knapsack1.txt?Expires=15377472'
#           '00&Signature=CPII3xWa~ASjHvMmlwoDURYHgCbHLXymz-8LEPMnQclYGm3E0~t9gNquuR2BM1VOb-44skwzN9afwT0USDZIu~X0K'
#           'vfzB1-~VoMC4Kl8e2BWzZPl8PJ8v-2XUo1XPGk-yBjSWdnA6hvaLe5aoW~pi~H32cAwuSSgYRDcDBWcBjo_&Key-Pair-Id=APKAJL'
#           'TNE6QMUY6HBC5A')

capacity, items = parse(raw)

print("\nResult: %s" % compute_optimal_knapsack_value(capacity, items))

print("\n--- Took %f seconds ---" % (time.time() - start_time))

# 2571817
