import torch
from torch.distributed import ReduceOp

# Initialize distributed environment (for this example, using CPU)
torch.distributed.init_process_group(backend='gloo')

# Create a tensor
tensor = torch.tensor([1.0, 2.0, 3.0], device=torch.device('cpu'))

# Use a safe reduce operation that does not violate any constraints
reduce_op = ReduceOp.SUM

# Call the API
result = torch.distributed.all_reduce(tensor, op=reduce_op)

print(result)

# Cleanup distributed environment
torch.distributed.destroy_process_group()