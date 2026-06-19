import torch

# Initialize distributed environment
torch.distributed.init_process_group(backend='gloo')

# Prepare valid input data
tensor = torch.tensor([1.0, 2.0], dtype=torch.float32)

# Call the API with SUM operation
result = torch.distributed.all_reduce(tensor, op=torch.distributed.ReduceOp.SUM)

print(result)