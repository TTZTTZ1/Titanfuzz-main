import torch

# Prepare input data
input_tensor = torch.randn(1, 10)

# Call the API
output = torch.nn.AdaptiveMaxPool1d((5,), return_indices=True)(input_tensor)