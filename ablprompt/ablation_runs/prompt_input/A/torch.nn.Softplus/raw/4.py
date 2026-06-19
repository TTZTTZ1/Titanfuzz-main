import torch
from torch.nn import Softplus

# Create an instance of Softplus
softplus = Softplus(beta=1, threshold=20)

# Example input tensor
input_tensor = torch.tensor([-1.0, 0.0, 1.0])

# Apply Softplus function to the input tensor
output_tensor = softplus(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor:", output_tensor)