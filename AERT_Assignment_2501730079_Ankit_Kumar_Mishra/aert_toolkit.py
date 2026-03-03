# AERT Toolkit
# Name: Ankit Kumar Mishra
# Roll no.: 2501730079
# Course: Data Structure


# Stack class

class StackADT:

    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if self.is_empty():
            print("Stack empty")
            return None
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            print("Stack empty")
            return None
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


# Factorial function
# base case when n is 0 or 1

def factorial(n):

    if n < 0:
        print("Invalid input for factorial")
        return None

    if n == 0 or n == 1:
        return 1

    # recursive call
    return n * factorial(n-1)


# Fibonacci part

naive_count = 0  
memo_count = 0  

# simple recursive fibonacci
def fib_naive(n):
    global naive_count
    naive_count += 1

    if n <= 1:
        return n

    return fib_naive(n-1) + fib_naive(n-2)


# fibonacci with memoization 
def fib_memo(n, memo):
    global memo_count
    memo_count += 1

    if n in memo:
        return memo[n]

    if n <= 1:
        memo[n] = n
    else:
        memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)

    return memo[n]


# Tower of Hanoi code
# recursive function to move disks

def hanoi(n, src, helper, dest, stack_obj):

    if n == 1:
        move = "Move disk 1 from " + src + " to " + dest
        print(move)
        stack_obj.push(move)
        return

    # first move n-1 disks to helper rod
    hanoi(n-1, src, dest, helper, stack_obj)

    move = "Move disk " + str(n) + " from " + src + " to " + dest
    print(move)
    stack_obj.push(move)

    # now move those n-1 disks to final destination
    hanoi(n-1, helper, src, dest, stack_obj)


# binary Search function

def binary_search(arr, key, low, high):

    if low > high:
        return -1

    # calculation for mid
    mid = (low + high) // 2
    print("Mid index:", mid)

    if arr[mid] == key:
        return mid

    elif key < arr[mid]:
        return binary_search(arr, key, low, mid - 1)

    else:
        return binary_search(arr, key, mid + 1, high)


# Main Function

def main():

    print("Stack ADT Testing")
    st = StackADT()
    st.push(5)
    st.push(15)
    print("size =", st.size())
    print("Top element:", st.peek())
    print("Pop value =", st.pop())
    print("Size after pop:", st.size())

    print("\nFactorial testing")
    nums = [0, 1, 5, 10]
    for num in nums:
        ans = factorial(num)
        print("Factorial:", num, "=", ans)

    print("\nFibonacci testing")

    test_values = [5, 10, 20, 30]

    for val in test_values:

        global naive_count, memo_count
        naive_count = 0
        memo_count = 0

        print("\nFor n =", val)

        ans1 = fib_naive(val)
        print("Naive fibonacci:", ans1)
        print("Total calls (naive):", naive_count)

        ans2 = fib_memo(val, {})
        print("Memo fibonacci:", ans2)
        print("Total calls (memo):", memo_count)

    print("\nTower of Hanoi for n=3")

    stack_for_hanoi = StackADT()
    hanoi(3, "A", "B", "C", stack_for_hanoi)

    print("Total moves:", stack_for_hanoi.size())

    print("\nBinary Search test")

    arr = [1, 3, 5, 7, 9, 11, 13]

    keys = [7, 1, 13, 2]

    for k in keys:
        result = binary_search(arr, k, 0, len(arr) - 1)
        print("Search", k, "Index =", result)

    empty = []
    print("Search in empty list:", binary_search(empty, 5, 0, len(empty) - 1))


if __name__ == "__main__":
    main()