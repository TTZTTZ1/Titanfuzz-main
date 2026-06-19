import torch
import torch.nn as nn

# Create a tensor
x = torch.tensor([-1.0, 0.0, 1.0], requires_grad=True)

# Apply Tanh function from torch.nn
tanh_function = nn.Tanh()
output = tanh_function(x)

print("Input:", x)
print("Output:", output)