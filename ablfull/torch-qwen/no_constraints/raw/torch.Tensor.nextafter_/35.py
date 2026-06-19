import torch

# Generate input data
x = torch.tensor(1.0)
y = torch.tensor(2.0)

# Call the API
result = x.nextafter(y)