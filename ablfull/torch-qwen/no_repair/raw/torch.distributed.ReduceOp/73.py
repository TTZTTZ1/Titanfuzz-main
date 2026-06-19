import torch.distributed as dist

dist.init_process_group(backend='gloo')
reduce_op = dist.ReduceOp.SUM
tensor = torch.tensor([1, 2, 3], dtype=torch.int)

dist.reduce(tensor, dst=0, op=reduce_op)
dist.destroy_process_group()