# cuquantum_benchmark_init

cuQuantum Benchmarks 的实验运行脚本：按量子比特数递增执行 QFT，或者运行 Qiskit/Aer 随机电路。这里不是 NVIDIA cuQuantum 或 CUDA-Q 的实现，也不包含 GPU 依赖。

[在线维护文档](https://xiaoshecode.github.io/xiaoshecode/repos/cuquantum_benchmark_init/)

## 环境与安装

Python 3.10+；Shell 脚本需要 Bash。GPU 测试需要兼容的 NVIDIA GPU、驱动、CUDA 和所选后端，具体版本以所使用的 [NVIDIA cuQuantum Benchmarks](https://github.com/NVIDIA/cuQuantum/tree/main/benchmarks) 版本为准。

先按上游说明准备环境，再指定上游 benchmarks 源码目录安装：

```bash
bash benchmark_env_install.sh /path/to/cuQuantum/benchmarks
cuquantum-benchmarks circuit --help
```

`cuquantum_env_install.sh` 是历史 CUDA-Q/Conda 环境配方，固定 CUDA 11.8 与 Python 3.11；CUDA-Q 与 cuQuantum Benchmarks 是不同项目。该配方未在本轮执行，不保证适合当前平台，不能替代上游安装步骤。

## 使用

```bash
python benchmark_test.py --start-qubits 1 --max-qubits 20 --timeout 300
NUM_QUBITS=12 BENCHMARK_NAME=random bash benchmarks.sh
```

QFT 默认使用 PennyLane Lightning GPU，超时为**每个子进程**的运行上限；超时后停止并返回 124，命令缺失返回 127，后端错误保留退出码。`--max-qubits` 限制递增范围，请按显存设置。`benchmarks.sh` 默认使用 Qiskit/Aer，额外 CLI 参数可放在脚本参数末尾。

## 目录与维护

| 路径 | 职责 |
| --- | --- |
| `benchmark_test.py` | 可导入的有界运行器及 CLI |
| `benchmarks.sh` | 单次随机电路示例 |
| `benchmark_env_install.sh` | 从指定上游目录安装 |
| `cuquantum_env_install.sh` | 历史环境参考 |
| `tests/` | 不依赖 GPU 的子进程边界回归测试 |

```bash
python -m unittest discover -s tests -v
python benchmark_test.py --help
```

测试使用模拟进程，验证终止、错误传播和参数；不证明 GPU 后端兼容、性能或显存容量。本轮没有运行真实 GPU 基准。仓库尚未声明开源许可证，复用前需明确许可。
