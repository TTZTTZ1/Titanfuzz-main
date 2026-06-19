import torch
tensor1 = torch.tensor([4.0, 3.0, 2.0])
tensor2 = torch.tensor([2.0, 1.0, 1.0])
result = torch.divide(tensor1, tensor2)
print(result)