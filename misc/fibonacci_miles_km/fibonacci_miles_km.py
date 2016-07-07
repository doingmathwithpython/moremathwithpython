'''
Demonstration of https://www.reddit.com/r/AskReddit/comments/4kz3di/whats_your_favourite_maths_fact/d3j55hv
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
 
def plot_km_miles_ratio(kms):
    miles_km = [1.6094*km/km for km in kms]
    plt.plot(miles_km, 'ro')

def estimate_kms(miles):
    approx_kms = []
    exact_kms = [1.6094*m for m in miles[1:]]
    for i in range(len(series)-1):
        approx_kms.append(series[i]+series[i+1])

    plt.figure(2)
    plt.plot(approx_kms, exact_kms, 'ro')
    plt.title('Approximating kilometers using fibonacci')


if __name__ == '__main__':
    # Number of fibonacci numbers
    num = 100
    series = fibo(num)
    plot_fibo_ratio(series)
    plot_km_miles_ratio(series)
    plt.figure(1)
    plt.title('Ratio between Fibonacci numbers & Golden ratio')
    plt.legend(['Fibonacci Numbers', 'Miles/Km'])
    estimate_kms(series)

    plt.show()
