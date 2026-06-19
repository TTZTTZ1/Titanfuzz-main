import torch

# Define the backend and operation type
backend = "gloo"  # NCCL is not used here to avoid conflicts
reduce_op_type = "SUM"

# Prepare the tensor
tensor = torch.tensor([1.0, 2.0, 3.0])

# Call the API
torch.distributed.reduce(tensor, op=torch.distributed.ReduceOp[reduce_op_type], group=torch.distributed.group.WORLD)