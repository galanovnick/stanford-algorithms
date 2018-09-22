from functools import reduce


def get_optimal_tree():
    for s in range(0, n):
        for i in range(0, n):
            if i + s >= n:
                break
            range_top = i + s + 1
            matrix[i + s][i] = min(map(
                (lambda r: reduce(
                    (lambda v1, v2: v1 + v2), weights[i:range_top]
                ) + get_matrix_value(r - 1, i) + get_matrix_value(i + s, r + 1)),
                range(i, range_top)))
    return matrix[n - 1][0]


def get_weight(index):
    return weights[index] if is_index_valid(index) else 0


def get_matrix_value(index_i, index_j):
    return matrix[index_i][index_j] if is_index_valid(index_i, index_j) else 0


def is_index_valid(*indices):
    return reduce((lambda i1, i2: 0 <= i1 < n and 0 <= i2 < n), indices)


def parse(strings):
    return list(map((lambda v: float(v)), strings.split('\n')))


raw = '0.05\n0.4\n0.08\n0.04\n0.1\n0.1\n0.23'
weights = parse(raw)
n = len(weights)
matrix = [[0 for j in range(0, n)] for i in range(0, n)]

print(get_optimal_tree())
print(matrix)
