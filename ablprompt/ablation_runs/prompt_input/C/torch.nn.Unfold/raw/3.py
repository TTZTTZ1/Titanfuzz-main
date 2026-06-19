import torch

# Define the input tensor
input_tensor = torch.randn(1, 1, 5, 5)

# Create an instance of Unfold
unfold = torch.nn.Unfold(kernel_size=2, stride=1, padding=0)

# Apply Unfold to the input tensor
output_tensor = unfold(input_tensor)

print(output_tensor.shape)  # Output should be [1, 4, 9]