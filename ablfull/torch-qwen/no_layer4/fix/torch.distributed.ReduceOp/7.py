import torch
from torch.distributed import ReduceOp
reduce_op = ReduceOp.SUM
tensor = torch.tensor([1, 2, 3], dtype=torch.float32)
backend = 'gloo'