import torch
tensor1 = torch.tensor([1.0, 2.0, 3.0])
tensor2 = torch.tensor([1.0, 2.5, 3.0])
result = tensor1.ne(tensor2)
print(result)