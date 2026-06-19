import torch

# Create a complex tensor
a = torch.tensor([[-0.5461 + 0.3347j, 0.1347 - 0.2347j], [-2.7266 + 0.8266j, -0.2746 - 0.1746j]])

# Compute the sine of the complex tensor
result = torch.sin(a)

print(result)