import torch

# Prepare valid input data
dtype = torch.float
from_val = 0
to_val = None

# Call the API
result = torch.tensor(5, dtype=dtype).random_(from_=from_val, to=to_val)
print(result)