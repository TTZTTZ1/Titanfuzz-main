import torch

# Generate input data
input_tensor = torch.randn(4, 4)

# Call the API
result = torch.std_mean(input_tensor, dim=0)
print(result)