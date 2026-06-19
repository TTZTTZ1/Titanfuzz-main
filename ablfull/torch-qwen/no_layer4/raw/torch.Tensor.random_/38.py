import torch

# Generate valid input data
dtype = 'float'
from_val = 0
to_val = 5
generator = None

# Call the API
tensor = torch.tensor(0, dtype=torch.float)
tensor.random_(from_val, to_val, generator=generator)