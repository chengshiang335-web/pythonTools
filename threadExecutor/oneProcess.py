import time

def job():
    total = 0
    for i in range(500_00000):
        total += i
    return total

start = time.time()

# 單線程跑 4 次
results = [job() for _ in range(4)]

end = time.time()
print("單線程 4次花費時間:", end - start)
print("結果:", results)