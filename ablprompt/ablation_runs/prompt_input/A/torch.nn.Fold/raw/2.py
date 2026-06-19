import torch

# Define input tensor and parameters for Fold operation
input_tensor = torch.randn(1, 4, 8, 8)
output_size = (2, 2)
kernel_size = (2, 2)
stride = (2, 2)

# Create an instance of Fold
fold = torch.nn.Fold(output_size, kernel_size, stride)

# Apply Fold to the input tensor
output_tensor = fold(input_tensor)

print("Input Tensor Shape:", input_tensor.shape)
print("Output Tensor Shape:", output_tensor.shape)