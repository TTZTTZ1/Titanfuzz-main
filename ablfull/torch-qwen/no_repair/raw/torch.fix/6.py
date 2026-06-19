import torch

# Generate input data
input_tensor = torch.tensor([-1.5, 0.3, 2.7])

# Call the API
output_tensor = torch.fix(input_tensor)