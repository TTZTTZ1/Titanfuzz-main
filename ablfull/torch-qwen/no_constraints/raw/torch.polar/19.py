import torch

# Generate input data
r = torch.tensor([1.0, 2.0])
theta = torch.tensor([0.0, 1.57])

# Call the API
result = torch.polar(r, theta)
print(result)