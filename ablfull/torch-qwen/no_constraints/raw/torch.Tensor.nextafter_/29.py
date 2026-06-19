import torch

# Prepare valid input data
x = torch.tensor(0.0)
y = torch.tensor(1.0)

# Call the API
result = x.nextafter(y)