import torch

# Generate input data
input_tensor = torch.tensor([0.5, -1.2, 3.7])

# Call the API
result = torch.special.round(input_tensor)

print(result)