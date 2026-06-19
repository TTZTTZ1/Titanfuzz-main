import torch

# Create a random input tensor
input_tensor = torch.randn(1, 3, 64, 64)

# Define the FractionalMaxPool2d layer
fractional_maxpool = torch.nn.FractionalMaxPool2d(kernel_size=3, output_ratio=(0.5, 0.5))

# Apply the fractional max pooling
output_tensor = fractional_maxpool(input_tensor)

print(output_tensor.shape)