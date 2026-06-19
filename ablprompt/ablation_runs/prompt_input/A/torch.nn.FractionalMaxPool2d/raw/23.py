import torch

# Create a random input tensor
input_tensor = torch.randn(1, 3, 64, 64)

# Define the FractionalMaxPool2d layer
fractional_max_pool = torch.nn.FractionalMaxPool2d(
    output_size=(32, 32),
    fractional_stride=(0.5, 0.5),
    pooling_ratio=(2.0, 2.0)
)

# Apply the FractionalMaxPool2d layer to the input tensor
output_tensor = fractional_max_pool(input_tensor)

print(output_tensor.shape)  # Output should be [1, 3, 32, 32]