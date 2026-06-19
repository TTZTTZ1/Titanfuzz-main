import torch

# Create a random tensor with both positive and negative values
input_tensor = torch.randn(5, 5)

# Compute the sign of each element in the tensor
signed_tensor = torch.sign(input_tensor)

print("Input Tensor:")
print(input_tensor)
print("\nSigned Tensor:")
print(signed_tensor)