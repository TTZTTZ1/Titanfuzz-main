import torch

# Prepare valid input data
reduce_op = torch.distributed.ReduceOp.SUM
tensor = torch.tensor([1.0, 2.0, 3.0])

# Call the API
result = reduce_op(tensor)
print(result)