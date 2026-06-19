import torch

# Generate valid input data
dtype = "float"
from_val = 0
to_val = None

# Call the API
result = torch.tensor([1], dtype=torch.float)
result.random_(from_=from_val, to=to_val)