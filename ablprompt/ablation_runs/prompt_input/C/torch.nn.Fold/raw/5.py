import torch

# Define the input tensor dimensions
input_tensor = torch.randn(1, 96, 8, 8)

# Define the Fold parameters
output_size = (16, 16)
kernel_size = 4
stride = 2
padding = 1

# Create the Fold layer
fold_layer = torch.nn.Fold(output_size=output_size, kernel_size=kernel_size, stride=stride, padding=padding)

# Apply the Fold layer to the input tensor
output_tensor = fold_layer(input_tensor)

print("Input Tensor Shape:", input_tensor.shape)
print("Output Tensor Shape:", output_tensor.shape)