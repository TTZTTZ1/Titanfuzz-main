import torch
from torch.nn import Softplus

# Create an instance of Softplus
softplus = Softplus(beta=1, threshold=20)

# Define some input data
input_data = torch.tensor([-1.0, 0.0, 1.0])

# Apply Softplus to the input data
output = softplus(input_data)

print(output)