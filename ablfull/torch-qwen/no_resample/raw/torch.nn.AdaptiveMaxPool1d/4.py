import torch

# Prepare valid input data
input_tensor = torch.randn(1, 5, 7)

# Call the API
output = torch.nn.AdaptiveMaxPool1d(output_size=3)(input_tensor)
print(output)