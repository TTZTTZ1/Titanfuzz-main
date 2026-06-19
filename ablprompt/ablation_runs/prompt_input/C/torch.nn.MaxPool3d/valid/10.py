import torch
from torch.nn import MaxPool3d

# Create a random input tensor
input_tensor = torch.randn(1, 3, 5, 5, 5)

# Define the MaxPool3d layer with specific parameters
max_pool = MaxPool3d(kernel_size=(2, 2, 2), stride=(2, 2, 2), padding=(1, 1, 1))

# Apply the max pooling operation
output_tensor = max_pool(input_tensor)

print(output_tensor.shape)