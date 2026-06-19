import torch

# Define input tensor and parameters for Fold
input_tensor = torch.randn(1, 32, 8, 8)  # Example input tensor of shape (batch_size, channels, height, width)
output_size = (4, 4)  # Desired output size after folding
kernel_size = (2, 2)  # Size of each kernel
stride = (2, 2)  # Stride of the convolution

# Create a Fold layer
fold_layer = torch.nn.Fold(output_size, kernel_size, stride)

# Apply the Fold layer to the input tensor
output_tensor = fold_layer(input_tensor)

print("Input Tensor Shape:", input_tensor.shape)
print("Output Tensor Shape:", output_tensor.shape)