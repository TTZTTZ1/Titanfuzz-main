import torch
torch.distributed.init_process_group(backend='gloo', init_method='tcp://localhost:29500', world_size=1, rank=0)
tensor = torch.tensor([1.0, 2.0, 3.0], dtype=torch.float32)
result = torch.distributed.reduce(tensor, op=torch.distributed.ReduceOp.SUM, dst=0)
print(result)