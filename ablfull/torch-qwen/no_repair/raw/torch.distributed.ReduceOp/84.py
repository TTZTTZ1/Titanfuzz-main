import torch

# Prepare input data
tensor = torch.tensor([1.0], dtype=torch.float32)
reduce_op = torch.distributed.ReduceOp.SUM
backend = 'gloo'  # Using 'gloo' to avoid constraints related to NCCL versions

# Call the API
result = torch.distributed.all_reduce(tensor, op=reduce_op, group=None, async_op=False)
print(result.item())