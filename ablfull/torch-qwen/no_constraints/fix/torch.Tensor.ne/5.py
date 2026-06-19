import torch
input_tensor = torch.tensor([1, 2, 3], dtype=torch.int64)
other_value = 2
result = input_tensor.ne(other_value)
print(result)