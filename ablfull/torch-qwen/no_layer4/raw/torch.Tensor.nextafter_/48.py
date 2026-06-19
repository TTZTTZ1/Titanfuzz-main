import torch

# Prepare input data
a = torch.tensor([1.0, 2.0], dtype=torch.float32)
b = torch.tensor([1.1, 2.2], dtype=torch.float32)

# Call the API
result = a.nextafter(b)
print(result)