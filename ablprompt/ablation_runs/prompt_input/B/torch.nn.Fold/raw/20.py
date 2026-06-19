import torch
from torch.nn import Fold

# Example usage of torch.nn.Fold
input_tensor = torch.randn(1, 64, 8, 8)
kernel_size = (2, 2)
output_size = (4, 4)
stride = (2, 2)

fold_layer = Fold(output_size=output_size, kernel_size=kernel_size, stride=stride)
output_tensor = fold_layer(input_tensor)

print(output_tensor.shape)  # Should be [1, 64, 4, 4]