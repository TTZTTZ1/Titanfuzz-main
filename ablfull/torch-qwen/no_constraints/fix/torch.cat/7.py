import torch
tensor1 = torch.randn(2, 3)
tensor2 = torch.randn(2, 3)
result = torch.cat((tensor1, tensor2), dim=0)