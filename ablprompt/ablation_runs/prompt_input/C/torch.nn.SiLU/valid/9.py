import torch

# Create a random tensor
input_tensor = torch.randn(3, 4)

# Apply SiLU activation
silu_layer = torch.nn.SiLU()
output_tensor = silu_layer(input_tensor)

print("Input Tensor:")
print(input_tensor)
print("Output Tensor after SiLU Activation:")
print(output_tensor)