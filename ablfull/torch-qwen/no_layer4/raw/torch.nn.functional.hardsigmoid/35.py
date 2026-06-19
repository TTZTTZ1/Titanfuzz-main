import torch

# Prepare input data
input_data = torch.tensor([-2.0, -1.0, 0.0, 1.0, 2.0], dtype=torch.float)

# Call the API
output = torch.nn.functional.hardsigmoid(input_data)
print(output)