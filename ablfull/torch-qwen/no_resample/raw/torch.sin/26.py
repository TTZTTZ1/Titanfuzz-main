import torch

# Generate input data
input_tensor = torch.tensor([0.0, 1.0, 2.0], dtype=torch.float)

# Call the API
result = torch.sin(input_tensor)
print(result)