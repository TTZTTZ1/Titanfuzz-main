import torch

# Prepare valid input data
dtype = 'int32'
tensor = torch.tensor([1, 2, 3], dtype=torch.int32)
op = 'SUM'
backend = 'gloo'

# Call the API
result = torch.distributed.reduce(tensor, op=op, group=None, async_op=False, backend=backend)
print(result)