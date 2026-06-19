import torch
from torch.distributed import ReduceOp

# Prepare valid input data
reduce_op = ReduceOp.SUM
tensor = torch.tensor([1.0, 2.0], dtype=torch.float32)

# Call the API
result = ReduceOp(reduce_op)