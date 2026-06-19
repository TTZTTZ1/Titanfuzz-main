import torch

# Create a random tensor
input_tensor = torch.randn(4, 4)

# Round the tensor elements to the nearest integer
rounded_tensor = torch.round(input_tensor)

print("Original Tensor:")
print(input_tensor)
print("\nRounded Tensor:")
print(rounded_tensor)