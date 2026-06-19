import torch

# Generate input data
input_tensor = torch.tensor([-1.0, 0.5, 1.0])

# Call the API
output_tensor = torch.nn.functional.hardsigmoid(input_tensor)