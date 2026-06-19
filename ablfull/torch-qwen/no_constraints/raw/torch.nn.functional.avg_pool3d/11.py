import torch

# Generate input data
input_tensor = torch.randn(1, 3, 4, 4, 4)

# Call the API
output_tensor = torch.nn.functional.avg_pool3d(input_tensor, kernel_size=2)