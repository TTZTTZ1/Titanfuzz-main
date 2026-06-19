import torch
from torch.nn import Fold

# Example usage of torch.nn.Fold
input_tensor = torch.randn(1, 32, 64, 64)
output_size = (16, 16)
kernel_size = (4, 4)
stride = (2, 2)

fold = Fold(output_size=output_size, kernel_size=kernel_size, stride=stride)
output_tensor = fold(input_tensor)

print(output_tensor.shape)  # Expected shape: torch.Size([1, 32, 16, 16])