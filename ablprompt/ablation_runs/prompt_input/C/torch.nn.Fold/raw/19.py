import torch

# Example input tensor of shape (N, C * ∏(kernel_size), L)
N = 1
C = 3
kernel_size = (2, 2)
L = 9
input_tensor = torch.randn(N, C * kernel_size[0] * kernel_size[1], L)

# Define Fold parameters
output_size = (5, 5)
dilation = 1
padding = 0
stride = 1

# Create Fold layer
fold_layer = torch.nn.Fold(output_size=output_size, kernel_size=kernel_size, dilation=dilation, padding=padding, stride=stride)

# Apply Fold layer to input tensor
output_tensor = fold_layer(input_tensor)

print("Input Tensor Shape:", input_tensor.shape)
print("Output Tensor Shape:", output_tensor.shape)