import torch

# Create a tensor
input_tensor = torch.randn(1, 1, 4, 4)

# Define the kernel size and stride for Unfold
kernel_size = (2, 2)
stride = (1, 1)

# Apply Unfold
unfolded_tensor = torch.nn.Unfold(kernel_size=kernel_size, stride=stride)(input_tensor)

print(unfolded_tensor)