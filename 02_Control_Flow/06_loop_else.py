# for-else: else runs if loop completes without break
def find_prime(numbers):
    for n in numbers:
        if n < 2:
            continue
        for d in range(2, int(n ** 0.5) + 1):
            if n % d == 0:
                break
        else:
            return n
    return None

# while-else
def search(items, target):
    i = 0
    while i < len(items):
        if items[i] == target:
            print(f"Found at {i}")
            break
        i += 1
    else:
        print("Not found")

if __name__ == "__main__":
    print(find_prime([4, 6, 8, 9, 11, 15]))
    search([1, 2, 3, 4], 3)
    search([1, 2, 3, 4], 10)