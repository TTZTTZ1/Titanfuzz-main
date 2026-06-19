import torch

# Create a random input tensor
input_tensor = torch.randn(3, 4)

# Apply the Tanh activation function
tanh_layer = torch.nn.Tanh()
output_tensor = tanh_layer(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor:", output_tensor)