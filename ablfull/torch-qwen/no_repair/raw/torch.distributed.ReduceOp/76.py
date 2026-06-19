import torch

# Prepare valid input data
backend = 'gloo'  # Avoiding constraints related to 'nccl'
reduce_op = 'SUM'

# Call the target API
result = torch.distributed.reduce_ops[reduce_op](tensor=None, op=reduce_op, async_op=False)
print(result)