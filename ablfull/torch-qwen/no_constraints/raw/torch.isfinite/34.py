import torch

# Prepare valid input data
input_tensor = torch.tensor([0.5, -float('inf'), float('nan'), 1.0])

# Call the API
result = torch.isfinite(input_tensor)

print(result)