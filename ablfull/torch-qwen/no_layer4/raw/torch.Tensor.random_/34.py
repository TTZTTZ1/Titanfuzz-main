import torch

# Generate valid input data
dtype = torch.float
from_val = 0
to_val = 5
generator = torch.Generator().manual_seed(42)

# Call the API
result = torch.tensor([0.5], dtype=dtype).random_(from_=from_val, to=to_val, generator=generator)
print(result)