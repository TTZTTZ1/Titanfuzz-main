import torch

# Example input tensor (batched image-like tensor)
input_tensor = torch.randn(1, 3, 6, 6)

# Define Unfold parameters
kernel_size = (3, 3)
stride = (2, 2)
padding = (1, 1)
dilation = (1, 1)

# Create an instance of Unfold
unfold = torch.nn.Unfold(kernel_size=kernel_size, stride=stride, padding=padding, dilation=dilation)

# Apply Unfold to the input tensor
output_tensor = unfold(input_tensor)

print(output_tensor.shape)  # Expected shape: (1, 9, 10)