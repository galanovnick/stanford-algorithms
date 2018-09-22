from utils.dataprovider import get


def parse(data):
    lines = data.split('\n')
    lines.pop(-1)
    meta = lines.pop(0)
    return [
        int(meta.split(' ')[0]),
        list(map((lambda item: {"value": int(item.split(' ')[0]), "weight": int(item.split(' ')[1])}), lines))
    ]


def compute_optimal_knapsack_value(capcity, items):
    amount = len(items)
    matrix = [[0 for i in range(0, capacity)] for j in range(0, amount)]

    for i in range(1, amount):
        weight = items[i]['weight']
        value = items[i]['value']
        for j in range(0, capacity):
            matrix[i][j] = max(matrix[i-1][j], matrix[i-1][j - weight] + value)

    return matrix[amount - 1][capacity - 1]


raw = get('https://d3c33hcgiwev3.cloudfront.net/_6dfda29c18c77fd14511ba8964c2e265_knapsack1.txt?Expires=1537747200'
          '&Signature=CPII3xWa~ASjHvMmlwoDURYHgCbHLXymz-8LEPMnQclYGm3E0~t9gNquuR2BM1VOb-44skwzN9afwT0USDZ'
          'Iu~X0KvfzB1-~VoMC4Kl8e2BWzZPl8PJ8v-2XUo1XPGk-yBjSWdnA6hvaLe5aoW~pi~H32cAwuSSgYRDcDBWcBjo_&Key-P'
          'air-Id=APKAJLTNE6QMUY6HBC5A')

capacity, items = parse(raw)

print(compute_optimal_knapsack_value(capacity, items))

# 4471248
