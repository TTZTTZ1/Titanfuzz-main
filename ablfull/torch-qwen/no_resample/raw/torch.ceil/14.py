import torch

# Generate input data
input_tensor = torch.tensor([-1.5, -0.2, 0.7, 2.3], dtype=torch.float)

# Call the API
result = torch.ceil(input_tensor)
print(result)