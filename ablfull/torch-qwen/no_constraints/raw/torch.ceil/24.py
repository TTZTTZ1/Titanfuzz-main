import torch

# Generate input data
input_data = torch.tensor([-1.5, -0.2, 0.0, 0.7, 1.9])

# Call the API
result = torch.ceil(input_data)

print(result)