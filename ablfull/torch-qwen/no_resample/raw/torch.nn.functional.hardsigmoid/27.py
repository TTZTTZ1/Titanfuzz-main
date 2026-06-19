import torch

# Prepare input data
input_tensor = torch.tensor([-1.0, 0.0, 1.0], dtype=torch.float)

# Call the API
output_tensor = torch.nn.functional.hardsigmoid(input_tensor)