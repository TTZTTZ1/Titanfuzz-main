import torch

# Prepare input data
input_tensor = torch.randn(3)
mat2_tensor = torch.randn(3)

# Call the API
result = torch.bmm(input_tensor.unsqueeze(0), mat2_tensor.unsqueeze(0)).squeeze()