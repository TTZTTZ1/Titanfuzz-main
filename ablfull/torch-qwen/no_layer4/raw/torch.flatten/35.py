import torch

# Generate input data
input_tensor = torch.randn(3, 4, 5)

# Prepare parameters
start_dim = 1
end_dim = 2

# Call the API
flattened_tensor = torch.flatten(input_tensor, start_dim=start_dim, end_dim=end_dim)
print(flattened_tensor)