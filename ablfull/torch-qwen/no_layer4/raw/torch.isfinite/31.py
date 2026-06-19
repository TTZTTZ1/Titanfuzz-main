import torch

# Generate input data
input_tensor = torch.tensor([1.0, 2.0, float('inf'), -float('inf')])

# Call the API
result = torch.isfinite(input_tensor)

print(result)