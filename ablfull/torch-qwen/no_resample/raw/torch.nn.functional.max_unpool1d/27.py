import torch

# Prepare input data
input_tensor = torch.randn(1, 3, 5)
indices = torch.tensor([[[0, 1, 2, 3, 4]]])

# Call the API
output = torch.nn.functional.max_unpool1d(input_tensor, indices, kernel_size=2)

print(output)