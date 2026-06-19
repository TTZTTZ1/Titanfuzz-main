import torch

# Generate input data
input_data = torch.tensor([2.0, 4.0, 8.0], dtype=torch.float)

# Call the API
result = torch.arccosh(input_data)
print(result)