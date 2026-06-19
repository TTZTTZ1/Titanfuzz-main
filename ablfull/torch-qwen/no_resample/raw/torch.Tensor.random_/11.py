import torch

# Prepare valid input data
dtype = 'int'
from_value = 0
to_value = 10

# Create a random tensor
result = torch.empty(5).random_(from_=from_value, to=to_value)
print(result)