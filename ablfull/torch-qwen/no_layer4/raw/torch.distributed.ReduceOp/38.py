import torch

# Prepare valid input data
reduce_op = torch.distributed.ReduceOp.SUM
backend = 'gloo'
tensor = torch.tensor([1.0, 2.0, 3.0])

# Call the API
torch.distributed.reduce(tensor, op=reduce_op, dst=0, group=torch.distributed.DEFAULT_GROUP)