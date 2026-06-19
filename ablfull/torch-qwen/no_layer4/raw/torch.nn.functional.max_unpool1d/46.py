import torch

input_tensor = torch.tensor([[[1., 2., 3.], [4., 5., 6.]]], dtype=torch.float32)
indices_tensor = torch.tensor([[[0, 1, 2], [0, 1, 2]]], dtype=torch.int64)
kernel_size = 2
stride = 1
padding = 0
output_size = (2, 3)

result = torch.nn.functional.max_unpool1d(input_tensor, indices_tensor, kernel_size, stride, padding, output_size)