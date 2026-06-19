import torch

# Prepare valid input data
input_tensor = torch.randn(1, 64, 50)

# Call the API
output = torch.nn.AdaptiveMaxPool1d((10,), return_indices=True)(input_tensor)