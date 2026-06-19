import torch

# Create a tensor
x = torch.tensor([-1.0, 0.0, 1.0])

# Apply sigmoid function
y = torch.sigmoid(x)

print(y)