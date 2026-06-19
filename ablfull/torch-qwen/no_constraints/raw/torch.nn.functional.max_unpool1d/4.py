import torch

input_tensor = torch.randn(1, 16)
indices = torch.argmax(torch.randn(1, 16), dim=1)
output = torch.nn.functional.max_unpool1d(input_tensor, indices, kernel_size=2)