import torch
from torch.nn import Softplus

# Create an instance of Softplus
softplus = Softplus(beta=1, threshold=20)

# Input tensor
input_tensor = torch.tensor([-1.0, 0.0, 1.0])

# Apply Softplus activation
output_tensor = softplus(input_tensor)

print(output_tensor)