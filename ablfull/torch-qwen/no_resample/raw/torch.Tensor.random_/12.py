import torch

# Prepare valid input data
dtype = 'float'
from_val = 0
to_val = None
generator = None

# Call the API
result = torch.tensor([1.0], dtype=torch.float).random_(from_=from_val, to=to_val, generator=generator)
print(result)