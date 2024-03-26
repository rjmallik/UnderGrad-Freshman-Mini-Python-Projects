from timeit import Timer
import random
from matplotlib import pyplot as plt


def bubbleSort(data):
    dataLen = len(data)
    for x in range(dataLen):
        for y in range(0, dataLen-x-1):
            if data[y] > data[y+1]:
                data[y], data[y+1] = data[y+1], data[y]

def mergeSort(data):
    if len(data) > 1:
       
        middle = len(data)//2
        left = data[:middle]
        right = data[middle:]

        mergeSort(left)
        mergeSort(right)
       
        a = b = c = 0
        while a < len(left) and b < len(right):
            if left[a] < right[b]:
                data[c] = left[a]
                a += 1
            else:
                data[c] = right[b]
                b += 1
            c += 1
        while a < len(left):
            data[c] = left[a]
            a += 1
            c += 1
        while b < len(right):
            data[c] = right[b]
            b += 1
            c += 1
def analyze(fxn, data):
    times = []
    for d in data:
        if fxn == "bubbleSort":
            t1 = Timer(lambda: bubbleSort(d))
            times.append(t1.timeit(number=5))
        elif fxn == "mergeSort":
            t2 = Timer(lambda: mergeSort(d))
            times.append(t2.timeit(number=5))
    return times

if __name__ == '__main__':

    # generate lists of random numbers from 0 to 500
    d1 = random.sample(range(0, 500), 10)
    d2 = random.sample(range(0, 500), 20)
    d3 = random.sample(range(0, 500), 50)
    d4 = random.sample(range(0, 500), 100)
    d5 = random.sample(range(0, 500), 200)

    # use random lists as input
    data = [d1, d2, d3, d4, d5]
    time = analyze('bubbleSort', data)
    plt.plot([len(i) for i in data], time, 'r')
   
    time = analyze('mergeSort', data)
    plt.plot([len(i) for i in data], time, 'b')
    plt.show()   