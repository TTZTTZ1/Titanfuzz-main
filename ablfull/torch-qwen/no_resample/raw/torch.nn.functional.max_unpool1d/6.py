import torch

# Prepare input data
input_tensor = torch.randn(1, 16)
indices = torch.argmax(input_tensor, dim=1, keepdim=True)
kernel_size = 2

# Call the API
output_tensor = torch.nn.functional.max_unpool1d(input_tensor, indices, kernel_size)

print(output_tensor)