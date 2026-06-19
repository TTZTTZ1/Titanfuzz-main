import torch

# Create a complex tensor
a = torch.tensor([[-0.5461 + 0.23j, 0.1347 + 0.89j], [-2.7266 - 0.12j, -0.2746 + 0.56j]])

# Compute the sine of each element in the complex tensor
result = torch.sin(a)

print(result)