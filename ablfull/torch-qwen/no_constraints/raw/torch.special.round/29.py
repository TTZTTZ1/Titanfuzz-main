import torch

# Generate input data
input_data = torch.tensor([-1.5, -0.5, 0.5, 1.5])

# Call the API
result = torch.special.round(input_data)

print(result)