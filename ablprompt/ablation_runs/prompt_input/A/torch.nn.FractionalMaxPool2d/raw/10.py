import torch

# Create a random input tensor
input_tensor = torch.randn(1, 3, 16, 16)

# Define the FractionalMaxPool2d layer
fractional_max_pool = torch.nn.FractionalMaxPool2d(
    kernel_size=4,
    output_ratio=(0.5, 0.5),
    fractional_stride=None,
    padding=0,
    ceil_mode=False
)

# Apply the FractionalMaxPool2d layer to the input tensor
output_tensor = fractional_max_pool(input_tensor)

print(output_tensor.shape)