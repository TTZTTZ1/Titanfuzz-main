import torch

# Create a random input tensor of shape (1, 3, 4, 5, 6)
input_tensor = torch.randn(1, 3, 4, 5, 6)

# Define the MaxPool3d layer with specific parameters
max_pool = torch.nn.MaxPool3d(kernel_size=(2, 2, 2), stride=(2, 2, 2), padding=(0, 0, 0))

# Apply the MaxPool3d layer to the input tensor
output_tensor = max_pool(input_tensor)

print("Input Tensor Shape:", input_tensor.shape)
print("Output Tensor Shape:", output_tensor.shape)