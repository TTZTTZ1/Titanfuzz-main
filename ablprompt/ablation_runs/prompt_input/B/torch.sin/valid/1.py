import torch

# Create a complex tensor
a = torch.tensor([[-0.5461 + 0.1347j, 0.1347 - 0.5461j], [-2.7266 + 0.2746j, -0.2746 - 2.7266j]])

# Compute the sine of each element
result = torch.sin(a)

print(result)