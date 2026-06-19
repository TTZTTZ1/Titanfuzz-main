import torch

# Prepare valid input data
input_tensor = torch.randn(1, 3, 4, 4, 4)
kernel_size = (2, 2, 2)
stride = (2, 2, 2)

# Call the API
output_tensor = torch.nn.functional.avg_pool3d(input_tensor, kernel_size=kernel_size, stride=stride)