import torch

# Generate valid input data
dtype = torch.float
from_val = 0
to_val = 1
generator = None

# Call the API
result = torch.tensor(random_=True, dtype=dtype, from_=from_val, to=to_val, generator=generator)