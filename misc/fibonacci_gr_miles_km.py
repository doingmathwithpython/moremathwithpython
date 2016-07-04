'''
The ration between consecutive fibonacci numbers and the ratio between a distance
measured in miles and kilometers tend to be ~ 1.6 (Golden Ratio)
'''

import matplotlib.pyplot as plt

def fibo(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    # n > 2
    a = 1
    b = 1
    # first two members of the series
    series = [a, b]
    for i in range(n):
        c = a + b
        series.append(c)
        a = b
        b = c

    return series

def plot_fibo_ratio(series):
    ratios = []
    for i in range(len(series)-1):
        ratios.append(series[i+1]/series[i])
    plt.plot(ratios, 'b*')
    plt.ylabel('Ratio')
    plt.xlabel('No.')
 
def plot_km_miles():
    kms = range(1, 100)
    miles_km = [1.6094*km/km for km in kms]
    plt.plot(miles_km, 'ro')


if __name__ == '__main__':
    # Number of fibonacci numbers
    num = 100
    series = fibo(num)
    plot_fibo_ratio(series)

    plot_km_miles()

    plt.title('Ratio between Fibonacci numbers & Golden ratio')
    plt.legend(['Fibonacci Numbers', 'Miles/Km'])
    plt.show()
