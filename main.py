import numpy as np
import matplotlib.pyplot as plt

def buckets_quantile(quantile, buckets):
    observations = buckets[len(buckets) - 1]['count']
    rank = observations * quantile

    b = 0
    for i in range(len(buckets)):
        if buckets[i]['count'] >= rank:
            b = i
            break

    count = buckets[b]['count'] - buckets[b-1]['count']
    rank = rank - buckets[b-1]['count']

    return buckets[b-1]['le'] + (buckets[b]['le'] - buckets[b-1]['le']) * (rank / count)

def k():
    return np.random.random()

if __name__ == '__main__':
    quantile = 0.75
    buckets = [
        {'le': 1, 'count': 5},
        {'le': 2, 'count': 10},
        {'le': 3, 'count': 15},
        {'le': 4, 'count': 20},
    ]

    aprox_q = buckets_quantile(quantile, buckets)
    text1 = f"Histogram's quantile: {aprox_q}\n"

    arr = np.concatenate([
        [x + k() for x in np.random.randint(0, 1, buckets[0]['count'])],
        [x + k() for x in np.random.randint(1, 2, buckets[1]['count'] - buckets[0]['count'])],
        [x + k() for x in np.random.randint(2, 3, buckets[2]['count'] - buckets[1]['count'])],
        [x + k() for x in np.random.randint(3, 4, buckets[3]['count'] - buckets[2]['count'])],
    ])

    precise_q = np.quantile(arr, quantile)
    text2 = f"Numpy's quantile: {precise_q}\n"

    fig, axs = plt.subplots(1, 1)
    axs.hist(arr, [0, 1, 2, 3, 4])
    axs.set_title(f"{text1} {text2}")
    fig.set_figheight(7)
    fig.set_figwidth(7)
    plt.show()
