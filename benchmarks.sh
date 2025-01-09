NUM_GPUS=1
BENCHMARK_NAME="random"
NUM_QUBITS=20
LOG2_NUM_NODE_GROUPS=0
LOG2_NUM_NODES_PER_GROUP=0
LOG2_NUM_PEERED_GPUS=0


# mpirun -n ${NUM_GPUS} 
cuquantum-benchmarks \
    circuit --frontend qiskit \
    --backend  aer
        # --benchmark ${BENCHMARK_NAME} \
        # --nqubits ${NUM_QUBITS} --ngpus 1 \
        # --cusvaer-global-index-bits ${LOG2_NUM_NODES_PER_GROUP},${LOG2_NUM_NODE_GROUPS} \
        # --cusvaer-p2p-device-bits ${LOG2_NUM_PEERED_GPUS}