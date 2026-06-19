import torch

# Prepare valid input data satisfying the constraint x >= 1
input_data = torch.tensor([2.0])

# Call the API
result = torch.arccosh(input_data)

print(result)