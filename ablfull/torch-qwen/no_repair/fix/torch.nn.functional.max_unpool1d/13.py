
import torch
input_tensor = torch.randn(1, 3, 4)
indices = torch.tensor([[[0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3]]])
kernel_size = 2
padding = 1
output = torch.nn.functional.max_unpool1d(input_tensor, indices, kernel_size, padding=padding)
print(output)
