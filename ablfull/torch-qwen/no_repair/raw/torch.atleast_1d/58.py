import torch

# Prepare valid input data
input_data = torch.tensor([1, 2, 3])

# Call the target API
result = torch.atleast_1d(input_data)

print(result)