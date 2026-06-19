import torch

# Generate input data
input_data = torch.randn(4, 4)

# Call the API
result = torch.slogdet(input_data)