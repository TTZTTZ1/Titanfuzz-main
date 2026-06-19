import torch

# Create a tensor with some values
x = torch.tensor([-1.0, 0.0, 1.0, -2.5, 3.0])

# Call the torch.sign function
result = torch.sign(x)

print(result)