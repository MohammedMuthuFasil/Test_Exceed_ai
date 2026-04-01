def bubble(a):
    n = len(a)
    for i in range(n):
        for j in range(0, n-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

# quick test
if __name__ == "__main__":
    print(bubble([64, 34, 25, 12, 22, 11, 90]))