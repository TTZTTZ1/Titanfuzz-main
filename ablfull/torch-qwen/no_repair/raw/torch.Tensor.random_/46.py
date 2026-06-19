import torch

# Prepare valid input data
dtype = 'float'
from_val = 0
to_val = 5

# Call the API
result = torch.tensor(0.0, dtype=torch.float).random_(from_=from_val, to=to_val)