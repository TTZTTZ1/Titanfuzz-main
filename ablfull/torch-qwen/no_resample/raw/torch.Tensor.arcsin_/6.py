import torch

# Generate input data
input_data = torch.tensor([0.5], dtype=torch.float32)

# Call the API
result = torch.Tensor.arcsin_(input_data)