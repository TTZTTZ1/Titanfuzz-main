import torch

# Create a random tensor
base_tensor = torch.randn(3, 4)

# Create an exponent tensor with the same shape as the base tensor
exponent_tensor = torch.randint(0, 5, (3, 4))

# Perform element-wise exponentiation using torch.pow
result_tensor = torch.pow(base_tensor, exponent_tensor)

print(result_tensor)