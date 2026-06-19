import torch

# Prepare valid input data
data = torch.tensor([[1, 2], [3, 4]])

# Call the API
result = torch.transpose(data, 0, 1)
print(result)