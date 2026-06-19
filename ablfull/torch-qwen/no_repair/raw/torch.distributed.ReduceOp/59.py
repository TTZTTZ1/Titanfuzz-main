import torch

# Prepare valid input data
reduce_op = "SUM"  # Avoiding operations not supported by all backends
tensor = torch.tensor([1.0, 2.0, 3.0], dtype=torch.float32)

# Call the API
torch.distributed.reduce(tensor, op=reduce_op)