import torch

# Generate input data
input_data = torch.tensor([-1.5, -0.2, 0.7, 1.8])

# Call the API
result = torch.fix(input_data)

print(result)