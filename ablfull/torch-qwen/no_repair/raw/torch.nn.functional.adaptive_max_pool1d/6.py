import torch

# Prepare input data
input_tensor = torch.randn(1, 3, 5)

# Call the API
output = torch.nn.functional.adaptive_max_pool1d(input_tensor, output_size=2)