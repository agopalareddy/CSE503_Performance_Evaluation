import time
import csv
from datetime import datetime

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes(limit):
    start_time = time.time()
    primes = [num for num in range(2, limit) if is_prime(num)]
    end_time = time.time()
    return len(primes), end_time - start_time

def run_test():
    results = []
    # Generate ranges from 1000 to 100000 in steps of 1000
    ranges = range(1000, 200001, 1000)
    
    for r in ranges:
        count, duration = find_primes(r)
        results.append([r, count, duration])
        print(f"Completed range: {r}")
    
    with open('python_results.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Range', 'Primes Found', 'Duration'])
        writer.writerows(results)

if __name__ == "__main__":
    run_test()
