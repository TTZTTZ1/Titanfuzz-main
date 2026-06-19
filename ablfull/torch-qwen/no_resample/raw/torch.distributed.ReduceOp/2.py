import torch

# Prepare valid input data
reduce_op = "SUM"
backend = "gloo"  # Using 'gloo' to avoid constraints related to 'NCCL'
tensor = torch.tensor([1.0, 2.0, 3.0])

# Call the API
result = torch.distributed.reduce(tensor, op=torch.distributed.ReduceOp[reduce_op], group=None)
print(result)