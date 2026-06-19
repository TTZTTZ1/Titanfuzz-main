import torch

# Prepare valid input data
dtype = 'int'
from_value = 0
to_value = None
generator = None

# Call the API
result = torch.Tensor([1]).random_(from_=from_value, to=to_value, generator=generator)
print(result)