import torch
import torch.nn as nn

# Create an instance of Softplus
softplus = nn.Softplus()

# Example input tensor
input_tensor = torch.tensor([-1.0, 0.0, 1.0])

# Apply Softplus activation function
output_tensor = softplus(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor after Softplus:", output_tensor)