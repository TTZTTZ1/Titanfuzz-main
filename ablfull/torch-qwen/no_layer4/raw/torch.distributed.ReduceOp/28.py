import torch

# Prepare input data
tensor = torch.tensor([1.0, 2.0, 3.0], dtype=torch.float32)
reduce_op = torch.distributed.ReduceOp.SUM
backend = 'gloo'

# Call the API
result = torch.distributed.reduce(tensor, op=reduce_op, group=torch.distributed.group.WORLD, async_op=False)
print(result)