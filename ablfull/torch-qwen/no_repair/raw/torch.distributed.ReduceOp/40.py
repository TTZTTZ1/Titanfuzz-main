import torch

# Prepare input data
op = torch.distributed.ReduceOp.SUM
backend = 'gloo'
tensor = torch.tensor([1.0, 2.0, 3.0])

# Call the API
result = torch.distributed.all_reduce(tensor, op=op, group=None, async_op=False)
print(result)