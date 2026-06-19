import torch

# Prepare valid input data
data_type = 'float'
from_val = 0
to_val = 1

# Call the API
tensor = torch.tensor(0.5, dtype=torch.float)
tensor.random_(from_=from_val, to=to_val)