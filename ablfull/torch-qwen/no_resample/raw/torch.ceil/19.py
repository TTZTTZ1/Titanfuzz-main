import torch

# Generate input data
input_data = torch.tensor([-1.5, -0.2, 0.7, 1.3], dtype=torch.float)

# Call the API
result = torch.ceil(input_data)
print(result)