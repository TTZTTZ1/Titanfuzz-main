import torch

# Prepare input data
input_tensor = torch.tensor([[0, 1], [2, 3]])

# Call the API
result = torch.any(input_tensor, dim=1)
print(result)