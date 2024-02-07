if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr = set(arr)
    
    arr = sorted(arr, reverse=True)
    print(arr[1])