import torch

# Prepare input data
input_tensor = torch.randn(1, 5)

# Call the API
output = torch.nn.AdaptiveMaxPool1d((3,), return_indices=True)(input_tensor)
print(output)