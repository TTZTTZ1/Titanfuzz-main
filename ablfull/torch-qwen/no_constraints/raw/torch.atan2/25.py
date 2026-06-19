import torch

# Generate input data
x = torch.tensor([0.5])
y = torch.tensor([-0.5])

# Call the API
result = torch.atan2(y, x)
print(result)