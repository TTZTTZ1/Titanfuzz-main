import torch

# Prepare valid input data
input_tensor = torch.randn(2, 3, 4)

# Call the API torch.flatten
result = torch.flatten(input_tensor, start_dim=1, end_dim=2)
print(result)