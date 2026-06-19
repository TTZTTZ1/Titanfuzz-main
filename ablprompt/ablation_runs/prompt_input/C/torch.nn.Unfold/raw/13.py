import torch
import torch.nn.functional as F

# Create a random input tensor
input_tensor = torch.randn(1, 3, 16, 16)

# Define the Unfold parameters
kernel_size = (3, 3)
stride = (1, 1)
padding = (1, 1)
dilation = (1, 1)

# Apply Unfold
unfolded_tensor = F.unfold(input_tensor, kernel_size=kernel_size, stride=stride, padding=padding, dilation=dilation)

print(unfolded_tensor.shape)  # Output should be (1, 3*3, 16*16)