import torch

# Create a random tensor
x = torch.randn(3, 4)

# Apply the sigmoid function
y = torch.sigmoid(x)

print(y)