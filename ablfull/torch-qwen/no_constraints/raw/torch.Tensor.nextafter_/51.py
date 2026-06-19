import torch

# Prepare valid input data
x = torch.tensor(0.0)
y = torch.tensor(0.1)

# Call the API
result = x.nextafter(y)

print(result)