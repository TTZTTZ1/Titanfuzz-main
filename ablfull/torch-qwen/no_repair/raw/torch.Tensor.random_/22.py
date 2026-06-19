import torch

# Prepare valid input data
dtype = 'int'
from_val = 0
to_val = 5

# Call the API
result = torch.tensor(0, dtype=torch.int).random_(from_=from_val, to=to_val)
print(result)