import torch

# Prepare valid input data
dtype = torch.int32
from_val = 1
to_val = None

# Call the API
tensor = torch.tensor(0, dtype=dtype)
tensor.random_(from_=from_val, to=to_val)
print(tensor)