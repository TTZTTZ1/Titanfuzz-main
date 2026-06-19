import torch
from torch.nn import Fold

# Example usage of torch.nn.Fold
input_tensor = torch.randn(1, 16, 8)  # Shape: (N, C * ∏(kernel_size), L)
output_size = (4, 4)
kernel_size = 2
stride = 2

fold_layer = Fold(output_size=output_size, kernel_size=kernel_size, stride=stride)

output_tensor = fold_layer(input_tensor)
print(output_tensor.shape)  # Expected shape: (1, 4, 4, 4)