import torch
input_data = torch.tensor([[[1.0, 2.0, 3.0]]], dtype=torch.float32)
indices = torch.tensor([[[0, 1, 2]]], dtype=torch.long)
kernel_size = 1
result = torch.nn.functional.max_unpool1d(input_data, indices, kernel_size=kernel_size)