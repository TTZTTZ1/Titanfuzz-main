import torch

# Prepare input data
input_data = torch.tensor([-float('inf'), -1.0, 0.0, 1.0])

# Call the API
result = torch.isneginf(input_data)

print(result)