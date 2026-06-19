import torch

# Prepare input data
input_tensor = torch.tensor([1.5, -0.4, 2.9])

# Call the API
result = torch.special.round(input_tensor)

print(result)