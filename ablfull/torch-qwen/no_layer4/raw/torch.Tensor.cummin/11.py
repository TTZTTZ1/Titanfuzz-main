import torch

# Generate input data
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float32)

# Call the API
result = input_tensor.cummin(dim=1)