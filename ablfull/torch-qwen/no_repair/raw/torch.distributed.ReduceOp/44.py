import torch

# Initialize the distributed environment
torch.distributed.init_process_group(backend='gloo')

# Create a tensor
tensor = torch.tensor([1, 2, 3], dtype=torch.float32)

# Perform a reduction operation using SUM
result = torch.distributed.reduce(tensor, op=torch.distributed.ReduceOp.SUM, dst=0)

if torch.distributed.get_rank() == 0:
    print(result)