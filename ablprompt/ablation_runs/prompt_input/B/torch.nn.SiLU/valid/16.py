import torch
from torch.nn import SiLU

# Create a random tensor
input_tensor = torch.randn(3, 4, requires_grad=True)

# Apply SiLU activation
siLU = SiLU()
output_tensor = siLU(input_tensor)

# Compute gradients
loss = output_tensor.sum()
loss.backward()

print("Input Tensor:", input_tensor)
print("Output Tensor:", output_tensor)
print("Gradients:", input_tensor.grad)