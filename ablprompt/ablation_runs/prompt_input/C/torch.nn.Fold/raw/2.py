import torch

# Example usage of torch.nn.Fold
input_tensor = torch.randn(1, 96, 8, 8)  # Shape: (N, C * ∏(kernel_size), L)
kernel_size = 3
output_size = (16, 16)

fold_layer = torch.nn.Fold(output_size=output_size, kernel_size=kernel_size, stride=1, padding=1)
output_tensor = fold_layer(input_tensor)

print(output_tensor.shape)  # Expected shape: (1, 32, 16, 16)