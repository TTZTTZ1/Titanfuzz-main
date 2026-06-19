import torch

# Generate valid input data
dtype = torch.float
from_value = 0
to_value = None
generator = None

# Call the API
result = torch.Tensor().random_(from_=from_value, to=to_value, dtype=dtype, generator=generator)