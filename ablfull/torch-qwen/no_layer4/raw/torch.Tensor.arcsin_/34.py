import torch

# Generate input data
input_tensor = torch.tensor([0.5])

# Call the API
output_tensor = torch.Tensor.arcsin_(input_tensor)