import torch

# Create a random tensor
input_tensor = torch.randn(3, 4)

# Unsqueeze the tensor at dimension 1
unsqueezed_tensor = torch.unsqueeze(input_tensor, 1)

print("Original Tensor Shape:", input_tensor.shape)
print("Unsqueezed Tensor Shape:", unsqueezed_tensor.shape)