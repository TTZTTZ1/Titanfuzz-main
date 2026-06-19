import torch
input_tensor = torch.tensor([1, 2, 3])
other_value = torch.tensor([1, 0, 3])
result = input_tensor.ne(other_value)
print(result)