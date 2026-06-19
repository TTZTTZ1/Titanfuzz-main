import torch

# Prepare input data
n = 4
input_tensor = torch.randn(n, n)

# Call the API
result = torch.slogdet(input_tensor)