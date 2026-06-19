import torch

# Generate input data
dtype = 'float'
from_val = 0
to_val = None
generator = None

# Call the API
tensor = torch.Tensor().random_(from_=from_val, to=to_val, dtype=dtype, generator=generator)
print(tensor)