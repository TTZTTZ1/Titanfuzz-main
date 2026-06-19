import torch

# Generate valid input data
reduce_op = torch.distributed.ReduceOp.SUM
tensor = torch.tensor([1, 2, 3], dtype=torch.float32)

# Call the API
result = reduce_op(tensor)