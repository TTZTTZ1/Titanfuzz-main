import torch

# Create a complex tensor
a = torch.tensor([[-0.5461 + 0.1j, 0.1347 - 0.2j], [-2.7266 + 0.3j, -0.2746 - 0.4j]])

# Compute the sine of each element
result = torch.sin(a)

print(result)