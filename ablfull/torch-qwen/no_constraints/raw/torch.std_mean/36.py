import torch

# Generate input data
input_data = torch.randn(5, requires_grad=True)

# Call the API
std, mean = torch.std_mean(input_data)