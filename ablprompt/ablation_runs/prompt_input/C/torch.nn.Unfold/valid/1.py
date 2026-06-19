import torch

# Create a random input tensor
input_tensor = torch.randn(1, 3, 16, 16)

# Define the Unfold parameters
kernel_size = (3, 3)
stride = (2, 2)
padding = (1, 1)
dilation = (1, 1)

# Apply Unfold
unfolded = torch.nn.Unfold(kernel_size=kernel_size, stride=stride, padding=padding, dilation=dilation)(input_tensor)

print(unfolded.shape)  # Output shape should be (1, 9, 7*7)