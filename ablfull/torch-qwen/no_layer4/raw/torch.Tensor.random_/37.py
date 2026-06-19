import torch

# Prepare input data
dtype = torch.int
from_value = 0
to_value = None
generator = None

# Call the API
result = torch.tensor(5, dtype=dtype).random_(from_=from_value, to=to_value, generator=generator)
print(result)