import torch

# Prepare valid input data
input_tensor = torch.randn(1, 3, 5)

# Call the API
output = torch.nn.AdaptiveMaxPool1d(output_size=3)(input_tensor)