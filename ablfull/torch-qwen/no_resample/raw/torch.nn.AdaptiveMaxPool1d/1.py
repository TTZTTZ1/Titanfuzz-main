import torch

# Prepare input data
input_tensor = torch.randn(1, 3, 5)

# Call the API
output = torch.nn.AdaptiveMaxPool1d((2,), return_indices=False)(input_tensor)