import torch
from torch.distributed import ReduceOp

# Import necessary components for distributed training
init_process_group(backend='gloo')

# Prepare input data
tensor = torch.tensor([1.0], requires_grad=True)

# Call the API with SUM operation using 'gloo' backend
result = ReduceOp.SUM(tensor)