import torch

# Create a random tensor
input_tensor = torch.randn(3, 4)

# Insert a new dimension at index 0
output_tensor = torch.unsqueeze(input_tensor, 0)

print("Original Tensor Shape:", input_tensor.shape)
print("Output Tensor Shape:", output_tensor.shape)