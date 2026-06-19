import torch

# Generate input data
input_tensor = torch.tensor([1.5, -0.4, 3.7])

# Call the API
result = torch.special.round(input_tensor)

print(result)