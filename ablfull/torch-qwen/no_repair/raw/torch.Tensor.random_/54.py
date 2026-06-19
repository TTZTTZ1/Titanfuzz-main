import torch

# Generate valid input data
dtype = 'int'
from_val = 0
to_val = 5

# Call the API
result = torch.Tensor([from_val]).random_(from_val, to_val)