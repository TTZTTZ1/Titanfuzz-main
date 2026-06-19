import torch

# Initialize the process group for distributed operations
torch.distributed.init_process_group(backend='gloo', init_method='env://')

# Prepare valid input data
tensor = torch.tensor([1.0, 2.0, 3.0], dtype=torch.float32)

# Call the API
result = torch.distributed.all_reduce(tensor, op=torch.distributed.ReduceOp.SUM)

print(result)