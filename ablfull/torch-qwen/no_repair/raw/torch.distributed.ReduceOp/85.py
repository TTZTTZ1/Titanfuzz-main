import torch

# Prepare valid input data
reduce_op = "SUM"
backend = "gloo"

# Call the API
result = torch.distributed.reduce(torch.tensor([1.0], device='cpu'), op=torch.distributed.ReduceOp[reduce_op], group=0)
print(result)