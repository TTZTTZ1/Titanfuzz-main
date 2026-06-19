import torch

# Define valid input parameters
reduce_op = torch.distributed.ReduceOp.SUM
backend = 'gloo'
tensor = torch.tensor([1.0])

# Call the API
torch.distributed.reduce(tensor, op=reduce_op, dst=0, group=torch.distributed.group.WORLD, async_op=False)