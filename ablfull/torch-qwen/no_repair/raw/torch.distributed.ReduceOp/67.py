import torch

# Prepare input data
reduce_op = torch.distributed.ReduceOp.SUM
backend = 'gloo'

# Call the API
result = torch.distributed.all_reduce(torch.tensor(5), op=reduce_op, group=torch.distributed.DEFAULT_GROUP)