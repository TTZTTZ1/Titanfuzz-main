import torch

# Define input tensor and parameters for Fold
input_tensor = torch.randn(1, 4, 20, 20)
output_size = (5, 5)
kernel_size = (3, 3)
stride = (2, 2)

# Create an instance of Fold
fold_layer = torch.nn.Fold(output_size, kernel_size, stride)

# Apply Fold to the input tensor
output_tensor = fold_layer(input_tensor)

print(output_tensor.shape)  # Output shape should be (1, 4*3*3, 6, 6)