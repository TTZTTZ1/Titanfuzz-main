import torch
tensor_a = torch.tensor([1.0, 2.0, 3.0])
tensor_b = torch.tensor([4.0, 5.0, 6.0])
result = tensor_a.add_(tensor_b)
print(result)