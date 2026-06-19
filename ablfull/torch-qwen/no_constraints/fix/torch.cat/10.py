import torch
tensor1 = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
tensor2 = torch.tensor([[5.0, 6.0], [7.0, 8.0]])
result = torch.cat((tensor1, tensor2), dim=0)
print(result)