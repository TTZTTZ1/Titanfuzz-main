import torch

# Generate input data
input_data = torch.tensor([0.0, 1.5708, 3.1416])

# Call the API
result = torch.sin(input_data)

print(result)