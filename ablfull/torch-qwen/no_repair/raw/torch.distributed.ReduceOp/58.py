import torch

# Prepare valid input data
op = "SUM"
tensor = torch.tensor([1.0, 2.0, 3.0], dtype=torch.float32)
backend = "gloo"

# Call the API
result = torch.distributed.reduce(tensor, op=op, dst=0, async_op=False, group=None, backend=backend)
print(result)