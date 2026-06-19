import torch

# Prepare input data
reduce_op = torch.distributed.ReduceOp.SUM
tensor = torch.tensor([1.0, 2.0, 3.0], dtype=torch.float32)
backend = 'gloo'

# Call the API
result = torch.distributed.reduce(tensor, op=reduce_op, group=None, async_op=False, backend=backend)
print(result)