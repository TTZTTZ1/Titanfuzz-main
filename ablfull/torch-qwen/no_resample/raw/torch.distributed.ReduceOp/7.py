import torch

# Prepare valid input data
reduce_op = torch.distributed.ReduceOp.SUM
backend = 'gloo'
tensor = torch.tensor([1.0, 2.0, 3.0])

# Call the API
result = reduce_op(tensor, op=reduce_op, group=torch.distributed.group.WORLD)
print(result)