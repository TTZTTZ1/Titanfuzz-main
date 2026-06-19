import torch

# Example usage of torch.nn.Fold
input_tensor = torch.randn(1, 16, 8, 8)  # Batch size=1, channels=16, height=8, width=8
kernel_size = (2, 2)
output_size = (4, 4)
stride = (2, 2)

fold_layer = torch.nn.Fold(output_size=output_size, kernel_size=kernel_size, stride=stride)
output_tensor = fold_layer(input_tensor)

print("Input Tensor Shape:", input_tensor.shape)
print("Output Tensor Shape:", output_tensor.shape)