import torch

# Define input tensor
input_tensor = torch.randn(1, 1, 5, 5)

# Create Unfold layer
unfold = torch.nn.Unfold(kernel_size=3, stride=1, padding=1)

# Apply Unfold
output_tensor = unfold(input_tensor)

print(output_tensor.shape)