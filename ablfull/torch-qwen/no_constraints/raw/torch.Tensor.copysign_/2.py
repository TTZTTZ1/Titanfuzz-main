import torch

# Generate input data
x = torch.tensor([-1.0, -2.0, 3.0])
y = torch.tensor([1.0, -2.0, 3.0])

# Call the API
result = x.copysign_(y)

print(result)