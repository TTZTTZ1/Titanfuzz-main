import torch

# Prepare valid input data
reduce_op = torch.distributed.ReduceOp.SUM
backend = 'gloo'
tensor = torch.tensor([1.0], device='cpu')

# Call the API
result = torch.distributed.reduce(tensor, op=reduce_op, group=torch.distributed.group.WORLD)