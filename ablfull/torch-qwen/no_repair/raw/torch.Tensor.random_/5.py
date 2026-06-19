import torch

# Prepare valid input data
dtype = 'float'
from_val = 0
to_val = 1

# Call the API
tensor = torch.Tensor().random_(from_=from_val, to=to_val)