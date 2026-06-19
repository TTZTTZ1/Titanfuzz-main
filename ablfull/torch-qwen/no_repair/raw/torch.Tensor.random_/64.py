import torch

# Generate input data
from_value = torch.tensor(0)
to_value = None

# Call the API
result = torch.Tensor().random_(from_=from_value, to=to_value)

print(result)