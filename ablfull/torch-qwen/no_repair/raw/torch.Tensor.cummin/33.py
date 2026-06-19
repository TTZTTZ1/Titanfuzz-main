import torch

# Prepare valid input data
input_tensor = torch.tensor([4, 2, 3, 1], dtype=torch.float32)

# Call the API
result = input_tensor.cummin(dim=0)