import torch

# Prepare valid input data
reduce_op = "SUM"
backend = "NCCL"
tensor = torch.tensor([1.0, 2.0, 3.0])

# Call the API
result = torch.distributed.reduce(tensor, op=reduce_op, group=torch.distributed.group.WORLD)
print(result)