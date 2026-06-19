import torch

# Generate input data
dtype = torch.int
from_val = 0
to_val = None
generator = None

# Call the API
result = torch.Tensor().random_(from_=from_val, to=to_val, generator=generator)
print(result)