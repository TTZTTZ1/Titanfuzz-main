import torch
import torch.nn as nn

# Create a Softplus layer with custom beta and threshold
softplus = nn.Softplus(beta=2.0, threshold=15.0)

# Example input tensor
input_tensor = torch.tensor([-1.0, 0.0, 1.0])

# Apply Softplus activation
output_tensor = softplus(input_tensor)

print(output_tensor)