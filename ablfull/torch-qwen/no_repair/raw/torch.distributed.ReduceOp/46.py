import torch

# Import necessary modules
from torch.distributed import ReduceOp, init_process_group, destroy_process_group

# Initialize process group
init_process_group(backend='gloo')

# Prepare valid input data
tensor = torch.tensor([1.0], dtype=torch.float32)

# Call the API with valid parameters
result = tensor.clone()
torch.distributed.reduce(result, op=ReduceOp.SUM, dst=0)

# Destroy the process group
destroy_process_group()