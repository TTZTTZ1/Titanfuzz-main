import torch

# Prepare valid input data
dtype = torch.float
from_val = 0
to_val = None
generator = None

# Call the API
result = torch.Tensor().random_(from=from_val, to=to_val, dtype=dtype, generator=generator)
print(result)