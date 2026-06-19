import torch

# Import necessary components
from torch.distributed import ReduceOp, init_process_group, all_reduce

# Initialize process group
init_process_group(backend='gloo')

# Prepare input tensor
tensor = torch.tensor([1.0, 2.0, 3.0])

# Select a supported operation
operation = ReduceOp.SUM

# Perform reduction
all_reduce(tensor, op=operation)

print(tensor)