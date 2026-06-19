import torch

# Prepare valid input data
A = torch.tensor([[4., 7.], [2., 6.]], dtype=torch.float)

# Call the API
result = torch.linalg.inv_ex(A, check_errors=True)