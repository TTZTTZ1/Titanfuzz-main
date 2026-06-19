import torch

# Generate input data
input_tensor = torch.tensor([-0.5, 0.0, 0.5], dtype=torch.float32)

# Call the API
result = torch.Tensor.arcsin_(input_tensor)