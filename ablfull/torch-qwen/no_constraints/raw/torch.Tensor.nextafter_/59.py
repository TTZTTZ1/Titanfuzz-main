import torch

# Prepare valid input data
input_tensor = torch.tensor([1.0], dtype=torch.float64)
eps = torch.tensor(1e-10, dtype=torch.float64)

# Call the API
result = torch.Tensor.nextafter(input_tensor, eps)