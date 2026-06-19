import torch

# Prepare valid input data
input_data = torch.tensor([2.0, 3.0])

# Call the target API
result = torch.arccosh(input_data)

print(result)