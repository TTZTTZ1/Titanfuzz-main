import torch

# Example input tensor (batched image-like tensor)
input_tensor = torch.randn(2, 3, 5, 5)

# Define Unfold parameters
kernel_size = (2, 2)
stride = (1, 1)
padding = (1, 1)
dilation = (1, 1)

# Create an instance of Unfold
unfold = torch.nn.Unfold(kernel_size=kernel_size, stride=stride, padding=padding, dilation=dilation)

# Apply Unfold to the input tensor
output_tensor = unfold(input_tensor)

print(output_tensor.shape)  # Output shape should be (2, 3*2*2, 9)