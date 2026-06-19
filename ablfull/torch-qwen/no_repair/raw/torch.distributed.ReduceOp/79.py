import torch

# Prepare valid input data
reduce_op = "SUM"
backend = "gloo"  # Avoiding NCCL constraints for simplicity
tensor = torch.tensor([1.0, 2.0, 3.0], dtype=torch.float32)

# Call the API
torch.distributed.reduce(tensor, op=reduce_op, group=None)