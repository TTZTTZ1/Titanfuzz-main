import torch

# Prepare valid input data: A tensor of values greater than or equal to 1
input_data = torch.tensor([2.0, 5.0])

# Call the API
result = torch.arccosh(input_data)
print(result)