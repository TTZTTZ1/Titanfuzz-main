import torch

# Generate input data
x = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)

# Call the API
result = torch.transpose(x, 0, 1)