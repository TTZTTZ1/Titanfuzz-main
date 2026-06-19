import torch

# Prepare valid input data
input_tensor = torch.randn(1, 10)

# Call the API
output = torch.nn.AdaptiveMaxPool1d((5,), return_indices=False)(input_tensor)