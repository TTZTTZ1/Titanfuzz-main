import torch

# Prepare input data
input_tensor = torch.tensor([0.5, -0.3], dtype=torch.float)

# Call the API
result = torch.sin(input_tensor)
print(result)