import torch

# Prepare valid input data
op = torch.distributed.ReduceOp.SUM
tensor = torch.tensor([1.0, 2.0, 3.0])

# Call the API
result = torch.distributed.all_reduce(tensor, op=op)