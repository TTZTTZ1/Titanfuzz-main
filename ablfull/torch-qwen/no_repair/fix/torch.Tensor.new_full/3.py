
import torch
size = (2, 3)
fill_value = 5.0
dtype = torch.float32
requires_grad = True
tensor = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]], dtype=dtype)
result = tensor.new_full(size, fill_value, dtype=dtype, requires_grad=requires_grad)
print(result)
