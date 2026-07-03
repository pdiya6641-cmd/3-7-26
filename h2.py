prices = [20000, 30000, 50000, 60000, 70000]
n = int(input("Enter Your Price: "))

low = 0
high = len(prices) - 1

while low <= high:
    mid = (low + high) // 2

    if prices[mid] >= n:
        ans = mid
        high = mid - 1
    else:
        low = mid + 1