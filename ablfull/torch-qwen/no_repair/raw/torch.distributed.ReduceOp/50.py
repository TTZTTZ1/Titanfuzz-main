import torch

# Initialize process group
torch.distributed.init_process_group(backend='gloo')

# Prepare input data
tensor = torch.tensor([1.0, 2.0], dtype=torch.float32)

# Call the API
result = torch.distributed.reduce(tensor, op=torch.distributed.ReduceOp.SUM)

print(result)