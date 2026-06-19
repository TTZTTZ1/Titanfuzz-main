
import torch
tensor = torch.randn(10)
split_size_or_number_of_splits = [2, 3, 5]
result = tensor.split(split_size_or_number_of_splits)
print(result)
