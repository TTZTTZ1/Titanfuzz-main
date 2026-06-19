import torch

# Prepare valid input data
input_tensor = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)

# Call the API
result = input_tensor.cummin(dim=0)