import torch

# Create a random tensor with both positive and negative values
input_tensor = torch.randn(5)

# Compute the sign of each element in the tensor
sign_tensor = torch.sign(input_tensor)

print("Input Tensor:", input_tensor)
print("Sign Tensor:", sign_tensor)