import torch

# Ensure NCCL is installed for proper functionality of the example
# pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu118

# Valid input parameters
reduce_op = torch.distributed.ReduceOp.SUM
backend = 'NCCL'
tensor = torch.randn(5)

# Call the API
result = torch.distributed.all_reduce(tensor, op=reduce_op, group=torch.distributed.group.WORLD)
print(result)