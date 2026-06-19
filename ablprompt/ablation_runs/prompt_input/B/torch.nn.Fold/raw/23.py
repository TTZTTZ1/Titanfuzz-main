import torch

# Example usage of torch.nn.Fold
input_tensor = torch.randn(1, 16, 8)
output_size = (16, 16)
kernel_size = (2, 2)
stride = (2, 2)

fold_layer = torch.nn.Fold(output_size=output_size, kernel_size=kernel_size, stride=stride)
output_tensor = fold_layer(input_tensor)

print(output_tensor.shape)  # Expected shape: torch.Size([1, 1, 16, 16])