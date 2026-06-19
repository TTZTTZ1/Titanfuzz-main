import torch.distributed as dist

# Initialize distributed environment (example setup)
dist.init_process_group(backend='nccl', init_method='env://')

# Prepare input tensor
tensor = torch.tensor([1.0], dtype=torch.float32, device='cuda')

# Call the API
result = dist.all_reduce(tensor, op=dist.ReduceOp.SUM)

# Clean up
dist.destroy_process_group()