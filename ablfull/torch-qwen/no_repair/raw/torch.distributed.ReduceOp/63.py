import torch
from torch.distributed import ReduceOp

# Prepare input data
tensor = torch.tensor([1.0, 2.0, 3.0], requires_grad=True)
reduce_op = ReduceOp.SUM
backend = 'gloo'

# Call the API
result = ReduceOp.reduce(tensor, op=reduce_op, async_op=False)

print(result)