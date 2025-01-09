import subprocess
import time

# 初始参数
nqubits = 1  # 初始量子比特数
max_time = 5 * 60  # 最大运行时间（5 分钟）
timeout = False  # 超时标志

# 循环运行基准测试
while not timeout:
    print(f"Running benchmark with nqubits = {nqubits}...")

    # 构建命令
    command = [
        "cuquantum-benchmarks", "circuit",
        "--benchmark", "qft",
        "--frontend", "pennylane",
        "--backend", "pennylane-lightning-gpu",
        "--nqubits", str(nqubits),
        "--ngpus", "1"
    ]

    # 记录开始时间
    start_time = time.time()

    # 运行命令
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running benchmark: {e}")
        break

    # 计算运行时间
    elapsed_time = time.time() - start_time
    print(f"Elapsed time: {elapsed_time:.2f} seconds")

    # 检查是否超时
    if elapsed_time > max_time:
        timeout = True
        print("Benchmark exceeded 5 minutes. Stopping.")
    else:
        # 增加量子比特数
        nqubits += 1
        print(f"Increasing nqubits to {nqubits}...")

print("Benchmark loop completed.")