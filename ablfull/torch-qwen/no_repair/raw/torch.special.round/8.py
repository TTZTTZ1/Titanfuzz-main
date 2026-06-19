import torch

# Generate input data
input_data = torch.tensor([1.5, -0.4, 2.7], dtype=torch.float)

# Call the API
result = torch.special.round(input_data)
print(result)