import torch

# Generate input data
input_tensor = torch.randn(1, 3, 8, 8, 8)

# Call the API
output = torch.nn.functional.avg_pool3d(input_tensor, kernel_size=2, stride=2, padding=1)