import torch
from torch.nn import Softplus

# Create an instance of the Softplus activation function
softplus = Softplus()

# Example input tensor
input_tensor = torch.tensor([-1.0, 0.0, 1.0])

# Apply the Softplus function to the input tensor
output_tensor = softplus(input_tensor)

print(output_tensor)