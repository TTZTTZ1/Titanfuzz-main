import torch

# Prepare input data
op = torch.distributed.ReduceOp.SUM
tensor = torch.tensor([1.0], dtype=torch.float32)

# Call the API
result = op(tensor)