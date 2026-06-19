import torch

# Generate input data
input_tensor = torch.randn(1, 64, 8)

# Call the API
output = torch.nn.functional.adaptive_max_pool1d(input_tensor, output_size=4)