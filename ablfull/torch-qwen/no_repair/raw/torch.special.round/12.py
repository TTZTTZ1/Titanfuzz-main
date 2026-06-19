import torch

# Prepare valid input data
input_data = torch.tensor([1.5, -2.3, 4.8])

# Call the API
result = torch.special.round(input_data)

print(result)