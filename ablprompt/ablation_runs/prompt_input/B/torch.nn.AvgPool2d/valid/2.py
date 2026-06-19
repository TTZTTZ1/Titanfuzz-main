import torch
from torch.nn import AvgPool2d

# Create a random input tensor
input_tensor = torch.randn(1, 3, 64, 64)

# Define the AvgPool2d layer with specific parameters
pool = AvgPool2d(kernel_size=(5, 5), stride=(2, 2), padding=(1, 1), ceil_mode=True, count_include_pad=False, divisor_override=None)

# Apply the pooling operation
output_tensor = pool(input_tensor)

print(output_tensor.shape)