import torch
tensor1 = torch.tensor([1.0, 2.0])
tensor2 = torch.tensor([3.0, 4.0])
result = tensor1.add_(tensor2)
print(result)