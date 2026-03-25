#ThreadPoolExecutor 實作（多執行緒）

import time
from concurrent.futures import ThreadPoolExecutor

def job():
    total = 0
    for i in range(500_00000):
        total += i
    return total

start = time.time()

with ThreadPoolExecutor(max_workers=4) as executor:
    results = list(executor.map(lambda _: job(), range(4)))

end = time.time()

print("多線程 花費時間:", end - start)