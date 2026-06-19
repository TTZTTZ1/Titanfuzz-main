import torch

# Prepare valid input data
dtype = 'float'
from_val = 0
to_val = None
generator = None

# Call the API
result = torch.Tensor().random_(from_=from_val, to=to_val, dtype=torch.get_default_dtype())
print(result)