import torch

# Prepare valid input data
input_tensor = torch.randn(1, 16)

# Call the API
output = torch.nn.AdaptiveMaxPool1d((8,), return_indices=False)(input_tensor)