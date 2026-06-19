import torch

# Prepare input data
input_tensor = torch.randn(1, 10)

# Call the API
output = torch.nn.AdaptiveMaxPool1d(output_size=5)(input_tensor)
print(output)