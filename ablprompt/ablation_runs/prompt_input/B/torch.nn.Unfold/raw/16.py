import torch

# Create a random input tensor
input_tensor = torch.randn(1, 1, 5, 5)

# Define the Unfold parameters
kernel_size = (2, 2)
stride = (1, 1)
padding = (1, 1)
dilation = (1, 1)

# Apply Unfold
unfolded_tensor = torch.nn.functional.unfold(input_tensor, kernel_size=kernel_size, stride=stride, padding=padding, dilation=dilation)

print(unfolded_tensor.shape)  # Output should be (1, 1*2*2, 9)