import torch

# Initialize the process group for distributed training
torch.distributed.init_process_group(backend='gloo')

# Prepare valid input data
tensor = torch.tensor([1.0, 2.0, 3.0], dtype=torch.float32)

# Call the API
result = torch.distributed.reduce(tensor, op=torch.distributed.ReduceOp.SUM, dst=0)

# Finalize the process group
torch.distributed.destroy_process_group()