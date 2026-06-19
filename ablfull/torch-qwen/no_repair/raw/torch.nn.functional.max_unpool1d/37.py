import torch

input_tensor = torch.tensor([[[1], [2], [3]]])
indices = torch.tensor([[[0], [1], [2]]])
kernel_size = 1
stride = 1
padding = 0

output = torch.nn.functional.max_unpool1d(input_tensor, indices, kernel_size, stride, padding)
print(output)