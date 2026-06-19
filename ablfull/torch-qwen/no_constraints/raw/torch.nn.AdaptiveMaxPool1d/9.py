import torch

# Prepare valid input data
input_tensor = torch.randn(1, 64, 8)

# Call the API
output = torch.nn.AdaptiveMaxPool1d(output_size=4)(input_tensor)