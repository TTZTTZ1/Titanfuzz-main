import torch

# Prepare valid input data
dtype = 'float'
from_value = 0
to_value = 1
generator = None

# Call the API
result = torch.Tensor().random_(from_=from_value, to=to_value, dtype=torch.float)
print(result)