import torch

# Prepare valid input data
input_data = torch.tensor([-float('inf'), 0.0, float('inf')])

# Call the API
result = torch.isneginf(input_data)

print(result)