import torch
from torch.distributed import ReduceOp
reduce_op = ReduceOp.SUM
tensor = torch.tensor([1.0, 2.0], dtype=torch.float32)
result = ReduceOp(reduce_op)