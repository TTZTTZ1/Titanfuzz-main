import torch

# Prepare valid input data
n = 3
A = torch.tensor([[4, 7], [2, 6]], dtype=torch.float)

# Call the API
result = torch.linalg.inv(A)