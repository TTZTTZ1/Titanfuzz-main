import torch

# Prepare valid input data
dtype = 'float'
from_value = 1
to_value = None
generator = None

# Call the API
result = torch.Tensor().random_(from_=from_value, to=to_value, dtype=torch.dtype[dtype], generator=generator)

print(result)