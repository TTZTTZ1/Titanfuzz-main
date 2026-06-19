import torch

# Prepare valid input data
dtype = torch.float32
from_val = 0
to_val = 10
generator = None

# Call the API
result = torch.zeros(1, dtype=dtype).random_(from_=from_val, to=to_val, generator=generator)