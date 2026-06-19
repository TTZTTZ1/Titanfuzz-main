import torch
input_tensor = torch.randn(4, 5)
split_result = input_tensor.split(split_size=[2, 2], dim=0)
print(split_result)