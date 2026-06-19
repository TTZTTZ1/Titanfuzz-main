import torch

# Generate input data
input_tensor = torch.tensor([0.5])

# Call the API
result = torch.Tensor.arcsin_(input_tensor)

print(result)