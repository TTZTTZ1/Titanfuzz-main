import torch

# Prepare valid input data
op = torch.distributed.ReduceOp.SUM
backend = 'gloo'  # Using 'gloo' as it supports BAND, BOR, BXOR and AVG
tensor = torch.tensor([1, 2, 3, 4], dtype=torch.float32)

# Call the API
torch.distributed.reduce(tensor, op=op, dst=0, async_op=False, backend=backend)