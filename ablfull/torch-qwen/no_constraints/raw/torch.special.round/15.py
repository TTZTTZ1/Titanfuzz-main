import torch

# Generate input data
input_data = torch.tensor([-1.5, -0.7, 0.2, 0.8, 1.4])

# Call the API
result = torch.special.round(input_data)

print(result)