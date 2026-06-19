import torch

# Prepare input data
input_data = torch.tensor([1.0, 2.0, float('inf'), -float('inf')])

# Call the API
result = torch.isfinite(input_data)

print(result)