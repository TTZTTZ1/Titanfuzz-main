import torch

# Generate input data
input_tensor = torch.tensor([-1.0, 0.0, 1.0], dtype=torch.float32)

# Call the API
output_tensor = torch.nn.functional.hardsigmoid(input_tensor)