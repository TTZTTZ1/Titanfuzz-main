
import torch
tensor = torch.randn(10)
split_size_or_number_of_splits = [2, 4, 4]
result = tensor.split(split_size_or_number_of_splits)
print(result)
