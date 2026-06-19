import torch

# Define backend and operation
backend = 'gloo'
reduce_op = 'SUM'

# Create tensor
tensor = torch.tensor([1.0, 2.0, 3.0], dtype=torch.float32)

# Ensure operation is supported by backend
if reduce_op == 'BAND' or reduce_op == 'BOR' or reduce_op == 'BXOR':
    assert backend != 'NCCL', f"{reduce_op} is not supported with backend {backend}"
if reduce_op == 'AVG':
    assert backend == 'NCCL' and torch.version.cuda >= '10.2', f"{reduce_op} requires NCCL backend and CUDA 10.2+"
if reduce_op == 'PREMUL_SUM':
    assert backend == 'NCCL' and torch.version.cuda >= '10.3', f"{reduce_op} requires NCCL backend and CUDA 10.3+"

# Call the API
output = torch.distributed.all_reduce(tensor, op=reduce_op)
print(output)