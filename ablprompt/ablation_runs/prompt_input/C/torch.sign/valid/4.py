import torch

# Create a tensor with mixed positive, negative, and zero values
input_tensor = torch.tensor([-5, 0, 3, -2, 0])

# Use torch.sign to get the sign of each element in the tensor
signed_tensor = torch.sign(input_tensor)

print("Input Tensor:", input_tensor)
print("Signed Tensor:", signed_tensor)