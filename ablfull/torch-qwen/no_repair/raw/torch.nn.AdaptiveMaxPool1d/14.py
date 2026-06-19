import torch

# Prepare valid input data
input_tensor = torch.randn(1, 5, 64)

# Call the API
output = torch.nn.AdaptiveMaxPool1d(output_size=(8,), return_indices=False)(input_tensor)