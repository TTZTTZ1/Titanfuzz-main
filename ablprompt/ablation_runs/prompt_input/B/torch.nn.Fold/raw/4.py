import torch

# Example usage of torch.nn.Fold
input_tensor = torch.randn(1, 96, 8)
output_size = (4, 4)
kernel_size = (3, 3)
stride = (2, 2)
padding = (1, 1)

fold_layer = torch.nn.Fold(output_size=output_size, kernel_size=kernel_size, stride=stride, padding=padding)
output_tensor = fold_layer(input_tensor)

print(output_tensor.shape)  # Expected shape: torch.Size([1, 256, 4, 4])