import torch

input_tensor = torch.tensor([[[1.0], [2.0], [3.0]]])
indices = torch.tensor([[[0]], [[1]], [[2]]])
kernel_size = 2

result = torch.nn.functional.max_unpool1d(input_tensor, indices, kernel_size=kernel_size)
print(result)