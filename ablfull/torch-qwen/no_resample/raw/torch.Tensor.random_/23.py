import torch

# Prepare valid input data
dtype = 'float'
from_value = 0
to_value = 1

# Call the API
tensor = torch.tensor(0.5, dtype=torch.float)
tensor.random_(from_=from_value, to=to_value)