import torch

# Prepare input data
input_tensor = torch.tensor([0.5, float('inf'), -float('inf'), float('nan')], dtype=torch.float32)

# Call the API
result = torch.isfinite(input_tensor)
print(result)