import torch

# Create a complex tensor
a = torch.tensor([[-0.5461 + 0.2j, 0.1347 + 0.3j], [-2.7266 + 0.4j, -0.2746 + 0.5j]])

# Compute the sine of each element in the complex tensor
result = torch.sin(a)

print(result)