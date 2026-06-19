import torch
from torch.nn import Fold

# Example usage of torch.nn.Fold
input_tensor = torch.randn(1, 96, 8, 8)  # Batch size=1, channels=96, height=8, width=8
kernel_size = (3, 3)
output_size = (8, 8)
stride = (1, 1)
padding = (1, 1)

fold_layer = Fold(output_size=output_size, kernel_size=kernel_size, stride=stride, padding=padding)
output_tensor = fold_layer(input_tensor)

print(output_tensor.shape)  # Should be [1, 96, 8, 8]