import torch
tensor1 = torch.tensor([4.0, 8.0, 12.0])
tensor2 = torch.tensor([2.0, 2.0, 2.0])
result = torch.divide(tensor1, tensor2)
print(result)