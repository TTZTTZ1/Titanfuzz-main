import torch
tensor = torch.tensor([1.0, 2.0, 3.0], dtype=torch.float32)
reduce_op = torch.distributed.ReduceOp.SUM
backend = 'gloo'