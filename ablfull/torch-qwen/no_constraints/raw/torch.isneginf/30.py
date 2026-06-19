import torch

# Generate input data
input_data = -float('inf')

# Call the API
result = torch.isneginf(input_data)

print(result)