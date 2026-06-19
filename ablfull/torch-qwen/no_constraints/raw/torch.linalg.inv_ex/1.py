import torch

# Generate input data
a = torch.tensor([[4., 7.], [2., 6.]], dtype=torch.float32)

# Call the API
result = torch.linalg.inv_ex(a)