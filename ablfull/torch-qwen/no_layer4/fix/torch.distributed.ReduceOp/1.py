import torch
reduce_op = torch.distributed.ReduceOp.SUM
backend = 'gloo'
tensor = torch.tensor([1.0, 2.0, 3.0])