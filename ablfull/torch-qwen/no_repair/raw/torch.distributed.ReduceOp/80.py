import torch

# Prepare input data satisfying all constraints
reduce_op = torch.distributed.ReduceOp.SUM
tensor = torch.tensor([1.0], dtype=torch.float32)
backend = 'gloo'

# Call the API
torch.distributed.reduce(tensor, op=reduce_op, async_op=False)