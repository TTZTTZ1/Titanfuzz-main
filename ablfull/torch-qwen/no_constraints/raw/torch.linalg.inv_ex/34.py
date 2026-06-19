import torch

# Generate input data
a = torch.tensor([[4.0, 7.0], [2.0, 6.0]], dtype=torch.float32)

# Call the API
result = torch.linalg.inv_ex(a)