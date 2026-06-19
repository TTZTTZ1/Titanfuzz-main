import torch

size = (2, 3)
fill_value = 5.0
dtype = torch.float32
requires_grad = True

tensor = torch.tensor([[1., 2., 3.], [4., 5., 6.]], dtype=dtype)
result = tensor.new_full(size, fill_value, dtype=dtype, requires_grad=requires_grad)
print(result)