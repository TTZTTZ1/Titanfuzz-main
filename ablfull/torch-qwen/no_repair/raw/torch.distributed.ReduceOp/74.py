import torch

# Initialize distributed environment
torch.distributed.init_process_group(backend='gloo')

# Create valid input data
reduce_op = torch.distributed.ReduceOp.SUM
tensor = torch.tensor([1.0])

# Call the API
torch.distributed.reduce(tensor, op=reduce_op)

# Clean up
torch.distributed.destroy_process_group()