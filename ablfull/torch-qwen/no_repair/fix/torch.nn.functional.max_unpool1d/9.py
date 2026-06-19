
import torch
input_tensor = torch.randn(1, 16)
indices_tensor = torch.randint(0, 17, (1, 16))
kernel_size = 3
stride = 1
padding = 0
output = torch.nn.functional.max_unpool1d(input_tensor, indices_tensor, kernel_size, stride, padding)
