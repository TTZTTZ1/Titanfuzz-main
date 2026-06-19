import torch

# Prepare input data
input_tensor = torch.randn(1, 3, 5)
indices_tensor = torch.tensor([[[0, 1, 2, 3, 4]]])

# Call the API
output_tensor = torch.nn.functional.max_unpool1d(input_tensor, indices_tensor, kernel_size=2, padding=1)

print(output_tensor)