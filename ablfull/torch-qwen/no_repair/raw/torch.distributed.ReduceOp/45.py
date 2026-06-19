import torch

# Prepare input data
reduce_op = "SUM"
backend = "gloo"  # Using 'gloo' to avoid constraints related to 'NCCL'
tensor = torch.tensor([1.0, 2.0, 3.0])

# Call the API
torch.distributed.reduce(tensor, op=reduce_op, group=torch.distributed.group.WORLD)