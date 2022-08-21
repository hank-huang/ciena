import json

"""
Simple script that computes first 1000 fibonacci numbers and saves in JSON format
"""


def gen_fib_numbers(n):

    a, b = 0, 1
    sequence = []

    for i in range(n):
        sequence.append(b)
        a, b = b, b + a

    return sequence


if __name__ == '__main__':
    fib = gen_fib_numbers(1000)
    fpath = '../app/fibtools/precomputed_numbers.json'
    with open(fpath, 'w', encoding='utf-8') as f:
        json.dump(fib, f, indent=4)

