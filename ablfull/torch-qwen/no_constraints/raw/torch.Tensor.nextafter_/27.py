import torch

# Prepare valid input data
a = torch.tensor(1.0)
b = torch.tensor(2.0)

# Call the API
result = a.nextafter(b)