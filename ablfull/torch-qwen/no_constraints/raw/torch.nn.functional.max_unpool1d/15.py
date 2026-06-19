import torch

# Task 2: Generate input data
input_tensor = torch.randn(1, 4, 6)
indices_tensor = torch.tensor([[[0, 1, 2, 3, 4, 5]]], dtype=torch.long)

# Task 3: Call the API
output_tensor = torch.nn.functional.max_unpool1d(input_tensor, indices_tensor, kernel_size=2, stride=2, padding=0)
print(output_tensor)