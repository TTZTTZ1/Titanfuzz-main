import torch

# Task 2: Prepare valid input data
dtype = torch.float32
tensor = torch.tensor([1.0, 2.0], dtype=dtype)
op = torch.distributed.ReduceOp.SUM
backend = 'gloo'

# Task 3: Call the API
torch.distributed.reduce(tensor, op=op, dst=0, group=torch.distributed.group.WORLD, async_op=False, backend=backend)