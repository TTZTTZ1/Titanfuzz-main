import torch

# Generate input data
x = torch.tensor([1.0], dtype=torch.float64)
y = torch.tensor([2.0], dtype=torch.float64)

# Call the API
result = x.nextafter(y)

print(result)