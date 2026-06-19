import torch

# Prepare input data
input_data = torch.tensor([-1.0, 0.0, 1.0], dtype=torch.float)

# Call the API
output = torch.nn.functional.hardsigmoid(input_data)