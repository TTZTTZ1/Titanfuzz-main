import torch

# Prepare valid input data
reduce_op = "SUM"
backend = "gloo"  # Using 'gloo' to avoid restrictions on BAND, BOR, BXOR, AVG, PREMUL_SUM
tensor = torch.tensor([1.0, 2.0, 3.0], dtype=torch.float32)

# Call the API
result = torch.distributed.reduce(tensor, op=reduce_op, group=None, async_op=False)
print(result)