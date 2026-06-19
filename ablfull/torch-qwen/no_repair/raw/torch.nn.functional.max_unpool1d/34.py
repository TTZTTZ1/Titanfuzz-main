import torch

input_tensor = torch.randn(1, 4, 5)
indices_tensor = torch.tensor([[[2], [3], [1], [0]]])
kernel_size = 2

output = torch.nn.functional.max_unpool1d(input_tensor, indices_tensor, kernel_size)