import torch

# Prepare valid input data
dtype = torch.float32
from_val = 0
to_val = 5
generator = torch.Generator().manual_seed(42)

# Call the API
tensor = torch.tensor(random_=True, dtype=dtype, from_=from_val, to=to_val, generator=generator)
print(tensor)