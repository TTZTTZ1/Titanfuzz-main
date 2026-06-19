import torch

# Prepare input data
input_tensor = torch.randn(1, 5, 64)

# Call the API
output = torch.nn.AdaptiveMaxPool1d((32,), return_indices=False)(input_tensor)