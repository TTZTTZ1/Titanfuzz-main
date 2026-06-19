import torch

# Prepare input data
input_data = torch.tensor([0.5, -0.7, 2.3])

# Call the API
result = torch.special.round(input_data)

print(result)