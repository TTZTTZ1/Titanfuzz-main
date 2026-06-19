import torch

# Prepare valid input data
a = torch.tensor([1.0], dtype=torch.float32)
b = 1.5

# Call the API
result = a.nextafter(b)
print(result)