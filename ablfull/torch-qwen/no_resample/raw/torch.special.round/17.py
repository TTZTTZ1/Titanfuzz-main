import torch

# Prepare input data
input_tensor = torch.tensor([1.5, -2.3, 4.7])

# Call the API
result = torch.special.round(input_tensor)

print(result)