import torch

# Prepare input data
reduce_op = torch.distributed.ReduceOp.SUM
backend = 'gloo'
tensor = torch.tensor([1, 2, 3], dtype=torch.float32)

# Call the API
result = torch.distributed.reduce(tensor, reduce_op=reduce_op, op=reduce_op, async_op=False)
print(result)