import torch

# Prepare input data
input_tensor = torch.randn(1, 64)

# Call the API
output = torch.nn.AdaptiveMaxPool1d(output_size=8)(input_tensor)
print(output)