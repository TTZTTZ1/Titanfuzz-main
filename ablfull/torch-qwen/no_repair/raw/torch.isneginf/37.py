import torch

# Generate input data
input_tensor = torch.tensor([-float('inf'), 0.5, float('nan')])

# Call the API
result = torch.isneginf(input_tensor)

print(result)