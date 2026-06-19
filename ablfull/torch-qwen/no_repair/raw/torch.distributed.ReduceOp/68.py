import torch

# Define input data
backend = 'gloo'
reduce_op = 'SUM'
tensor = torch.tensor([1.0, 2.0, 3.0], device='cpu')

# Call the API
result = torch.distributed.reduce(tensor=tensor, op=reduce_op, async_op=False)

print(result)