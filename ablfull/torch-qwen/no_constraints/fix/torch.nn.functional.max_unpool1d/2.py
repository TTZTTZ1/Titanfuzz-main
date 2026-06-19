import torch
input_tensor = torch.randn(1, 16)
indices = torch.randint(0, 17, (1, 16))
output = torch.nn.functional.max_unpool1d(input_tensor, indices, kernel_size=2)