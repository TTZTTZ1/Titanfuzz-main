import torch
tensor1 = torch.tensor([1.0, 2.0, 3.0])
tensor2 = torch.tensor([4.0, 5.0, 6.0])
result = torch.Tensor.cross(tensor1, tensor2)
print(result)