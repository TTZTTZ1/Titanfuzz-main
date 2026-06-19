import torch
from torch import nn

# Create an instance of Softplus with custom beta and threshold
softplus = nn.Softplus(beta=2.0, threshold=30.0)

# Example input tensor
input_tensor = torch.tensor([-1.0, 0.0, 1.0], requires_grad=True)

# Apply Softplus activation
output = softplus(input_tensor)

# Print the output
print("Output:", output)

# Compute gradients
loss = output.sum()
loss.backward()

# Print the gradients
print("Gradients:", input_tensor.grad)