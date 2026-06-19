import torch

# Generate input data
dtype = torch.float
from_val = 0
to_val = 5
generator = None

# Call the API
result = torch.tensor(0.0, dtype=dtype).random_(from_=from_val, to=to_val, generator=generator)