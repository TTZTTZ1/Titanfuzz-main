import torch

# Example usage of torch.nn.Fold
input_tensor = torch.randn(1, 96, 7, 7)  # Batch size 1, 96 channels, 7x7 grid
kernel_size = (3, 3)
output_size = (14, 14)
stride = (2, 2)

fold = torch.nn.Fold(output_size=output_size, kernel_size=kernel_size, stride=stride)
output_tensor = fold(input_tensor)

print(output_tensor.shape)  # Should be [1, 96, 14, 14]