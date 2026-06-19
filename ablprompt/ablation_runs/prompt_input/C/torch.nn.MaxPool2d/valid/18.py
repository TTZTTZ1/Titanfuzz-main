import torch

# Create a random input tensor
input_tensor = torch.randn(1, 3, 32, 32)

# Define MaxPool2d layer
max_pool = torch.nn.MaxPool2d(kernel_size=3, stride=2, padding=1)

# Apply max pooling
output_tensor = max_pool(input_tensor)

print(output_tensor.shape)