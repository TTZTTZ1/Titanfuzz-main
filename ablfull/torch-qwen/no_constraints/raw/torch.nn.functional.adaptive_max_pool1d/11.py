import torch

# Prepare valid input data
input_tensor = torch.randn(1, 5, 64)  # Shape: [batch_size, channels, length]

# Call the API
output_tensor = torch.nn.functional.adaptive_max_pool1d(input_tensor, output_size=8)

print(output_tensor.shape)  # Expected shape: [1, 5, 8]