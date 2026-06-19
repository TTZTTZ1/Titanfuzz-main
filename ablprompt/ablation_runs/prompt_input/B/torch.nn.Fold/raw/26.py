import torch
from torch.nn import Fold

# Example usage of torch.nn.Fold
input_tensor = torch.randn(1, 96, 8)
output_size = (16, 16)
kernel_size = 3
stride = 2
padding = 1

fold_layer = Fold(output_size=output_size, kernel_size=kernel_size, stride=stride, padding=padding)
output_tensor = fold_layer(input_tensor)

print(output_tensor.shape)  # Expected shape: torch.Size([1, 48, 16, 16])