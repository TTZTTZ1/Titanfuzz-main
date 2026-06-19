import torch

# Generate input data
input_tensor = torch.randn(5, 5)

# Call the API
result = torch.slogdet(input_tensor)