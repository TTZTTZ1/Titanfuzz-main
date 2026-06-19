import torch

# Prepare valid input data
input_tensor = torch.randn(1, 3, 4)

# Call the API
output = torch.nn.AdaptiveMaxPool1d(output_size=2)(input_tensor)