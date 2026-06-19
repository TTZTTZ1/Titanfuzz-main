import torch

# Prepare valid input data
dtype = torch.float
from_val = 0
to_val = 10

# Call the API
result = torch.tensor(random_=True, dtype=dtype, from_=from_val, to=to_val)