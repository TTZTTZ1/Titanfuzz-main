import torch

# Prepare input data
input_data = torch.randn(1, 1, 5, 5, 5)

# Define parameters
kernel_size = (2, 2, 2)
stride = (1, 1, 1)
padding = (1, 1, 1)

# Call the API
output = torch.nn.functional.avg_pool3d(input_data, kernel_size, stride, padding)