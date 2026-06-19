import torch

# Prepare valid input data
tensor = torch.tensor([1.0], dtype=torch.float32)
dst = 0

# Call the API
result = torch.distributed.reduce(tensor, dst=dst, op=torch.distributed.ReduceOp.SUM)