import torch

# Prepare valid input data
dtype = torch.float
from_value = 0
to_value = 5
generator = torch.Generator().manual_seed(42)

# Call the API
result = torch.tensor(random_=(from_value, to_value), dtype=dtype, generator=generator)
print(result)