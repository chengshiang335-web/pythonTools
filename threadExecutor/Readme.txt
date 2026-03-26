#多序
# ThreadPoolExecutor 的差別：
# ThreadPoolExecutor → 4 個線程共享同一個 GIL（CPU 密集型任務沒加速）
# multiprocessing.Pool → 4 個進程，各自有 GIL → 可以同時跑 4 次 CPU 密集任務，真正利用多核 CPU
# | 版本                            | 執行緒/進程 | 是否受 GIL 影響 | CPU 密集型效能    |
# | ----------------------------    | ------ | ---------- | ------------ |
# | 單線程                          | 1        |有          | 最慢           |
# | 多線程 (`ThreadPoolExecutor`)   | 4 線程   | 有          | 與單線程差不多      |
# | 多進程 (`multiprocessing.Pool`) | 4 進程   | 無          | 快很多，利用多核 CPU |
