import torch

# Prepare valid input data
input_data = torch.tensor([[1, 2], [3, 4]])

# Call the API
result = input_data.ravel()

print(result)