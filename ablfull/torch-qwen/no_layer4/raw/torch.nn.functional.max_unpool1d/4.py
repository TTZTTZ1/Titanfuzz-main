import torch

input_tensor = torch.randn(1, 4, 5)
indices_tensor = torch.tensor([[[0, 1, 2, 3, 4]]])
kernel_size = 2
stride = 2
padding = 0

output = torch.nn.functional.max_unpool1d(input_tensor, indices_tensor, kernel_size, stride, padding)