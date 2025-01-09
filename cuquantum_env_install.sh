cuda_version=11.8.0 # set this variable to version 11.x (where x >= 8) or 12.x
conda create -y -n cudaq-env python=3.11 pip
conda install -y -n cudaq-env -c "nvidia/label/cuda-${cuda_version}" cuda
conda install -y -n cudaq-env -c conda-forge mpi4py openmpi cxx-compiler
conda env config vars set -n cudaq-env LD_LIBRARY_PATH="$CONDA_PREFIX/envs/cudaq-env/lib:$LD_LIBRARY_PATH"
conda env config vars set -n cudaq-env MPI_PATH=$CONDA_PREFIX/envs/cudaq-env
conda activate cudaq-env
pip install cudaq
source $CONDA_PREFIX/lib/python3.11/site-packages/distributed_interfaces/activate_custom_mpi.sh