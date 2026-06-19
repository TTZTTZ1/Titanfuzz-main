import torch
tensor1 = torch.tensor([1.0, 2.0])
tensor2 = torch.tensor([4.0, 5.0])
alpha = 0.5
result = tensor1.lerp_(tensor2, alpha)
print(result)