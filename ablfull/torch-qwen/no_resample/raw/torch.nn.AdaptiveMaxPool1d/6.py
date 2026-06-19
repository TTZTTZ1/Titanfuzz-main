import torch

# Prepare valid input data
input_tensor = torch.randn(1, 4, 5)

# Call the API
output = torch.nn.AdaptiveMaxPool1d((3,), return_indices=False)(input_tensor)