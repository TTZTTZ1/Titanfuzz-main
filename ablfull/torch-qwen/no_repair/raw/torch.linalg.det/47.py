import torch

# Prepare valid input data
A = torch.tensor([[4.0, 7.0], [2.0, 6.0]], dtype=torch.float)

# Call the target API
result = torch.linalg.det(A)
print(result)