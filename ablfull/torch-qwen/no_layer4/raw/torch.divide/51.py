import torch

# Prepare valid input data
input_tensor = torch.tensor([4.0, 8.0], dtype=torch.float32)
other_tensor = torch.tensor([2.0, 2.0], dtype=torch.float32)

# Call the API
result = torch.divide(input_tensor, other_tensor)