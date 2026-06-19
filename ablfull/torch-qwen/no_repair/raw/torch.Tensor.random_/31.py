import torch

# Prepare input data
dtype = 'float'
from_val = 0
to_val = None

# Call the API
result = torch.Tensor().random_(from_=from_val, to=to_val)
print(result)