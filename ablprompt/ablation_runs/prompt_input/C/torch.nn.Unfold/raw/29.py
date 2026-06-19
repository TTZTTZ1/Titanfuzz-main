import torch

# Create a random input tensor
input_tensor = torch.randn(1, 3, 8, 8)

# Define the Unfold parameters
kernel_size = (3, 3)
stride = (1, 1)
padding = (1, 1)
dilation = (1, 1)

# Apply Unfold
unfolded_tensor = torch.nn.functional.unfold(input_tensor, kernel_size, stride, padding, dilation)

print(unfolded_tensor.shape)  # Expected shape: [1, 9, 64]