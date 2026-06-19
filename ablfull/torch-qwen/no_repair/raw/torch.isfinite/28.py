import torch

# Generate a tensor of random values to ensure it's finite
input_tensor = torch.randn(5, 5)

# Call the API
result = torch.isfinite(input_tensor)
print(result)