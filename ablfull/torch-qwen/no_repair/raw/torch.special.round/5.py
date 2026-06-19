import torch

# Prepare valid input data
input_data = torch.tensor([1.5, -0.4, 2.9])

# Call the API
result = torch.special.round(input_data)

print(result)