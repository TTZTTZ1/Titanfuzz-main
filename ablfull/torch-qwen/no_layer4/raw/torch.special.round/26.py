import torch

# Prepare input data
input_tensor = torch.tensor([1.5, 2.3, -0.7, 4.8])

# Call the API
result = torch.special.round(input_tensor)

print(result)