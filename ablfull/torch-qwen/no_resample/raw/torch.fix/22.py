import torch

# Generate input data
input_tensor = torch.tensor([-1.5, -0.2, 0.7, 2.3])

# Call the API
result = torch.fix(input_tensor)