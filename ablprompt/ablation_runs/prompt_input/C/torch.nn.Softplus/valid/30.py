import torch
import torch.nn as nn

# Create an instance of Softplus with custom beta and threshold
softplus = nn.Softplus(beta=0.5, threshold=10.0)

# Example input tensor
input_tensor = torch.tensor([-1.0, 0.0, 1.0])

# Apply Softplus activation
output_tensor = softplus(input_tensor)

print("Input:", input_tensor)
print("Output:", output_tensor)