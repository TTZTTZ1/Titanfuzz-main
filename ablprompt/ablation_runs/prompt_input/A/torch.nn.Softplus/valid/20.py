import torch
from torch.nn import Softplus

# Create an instance of Softplus
softplus = Softplus()

# Define some input data
input_data = torch.tensor([-1.0, 0.0, 1.0])

# Apply Softplus activation to the input data
output_data = softplus(input_data)

print(output_data)