import torch
from torch.distributed import ReduceOp

# Prepare valid input data
reduce_op = ReduceOp.SUM
tensor = torch.tensor([1, 2, 3], dtype=torch.float32)
backend = 'gloo'

# Call the API
result = torch.distributed.all_reduce(tensor, op=reduce_op, backend=backend)
print(result)