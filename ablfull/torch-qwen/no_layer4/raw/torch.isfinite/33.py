import torch

# Prepare valid input data
input_tensor = torch.tensor([1.0, float('inf'), -float('inf'), float('nan')], dtype=torch.float32)

# Call the API
result = torch.isfinite(input_tensor)
print(result)