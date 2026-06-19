import torch

# Create a random input tensor of shape (1, 1, 4, 4)
input_tensor = torch.randn(1, 1, 4, 4)

# Define the Unfold layer with specific parameters
unfold = torch.nn.Unfold(kernel_size=2, stride=1, padding=1)

# Apply the Unfold operation to the input tensor
output_tensor = unfold(input_tensor)

print(output_tensor.shape)  # Expected output shape: torch.Size([1, 4, 9])