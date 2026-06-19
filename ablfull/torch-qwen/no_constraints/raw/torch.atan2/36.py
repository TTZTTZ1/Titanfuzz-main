import torch

# Generate input data
x = torch.tensor(1.0)
y = torch.tensor(0.5)

# Call the API
result = torch.atan2(y, x)