import torch

# Prepare valid input data
dtype = torch.float
from_val = 0
to_val = None
generator = None

# Call the API
result = torch.tensor(0.5, dtype=dtype)
result.random_(from_=from_val, to=to_val, generator=generator)
print(result)