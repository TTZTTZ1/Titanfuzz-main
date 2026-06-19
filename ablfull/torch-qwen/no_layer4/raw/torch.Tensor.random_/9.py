import torch

# Prepare valid input data
dtype = torch.float
from_value = 0
to_value = None
generator = None

# Call the API
result = torch.tensor(0, dtype=dtype).random_(from_=from_value, to=to_value, generator=generator)