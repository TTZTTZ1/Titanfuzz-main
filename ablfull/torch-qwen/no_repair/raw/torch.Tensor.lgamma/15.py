import torch

# Prepare valid input data
input_data = torch.tensor([0.5, 1.0, 2.0])

# Call the API
result = torch.lgamma(input_data)

print(result)