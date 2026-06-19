import torch
input1 = torch.randn(2, 3, 4)
input2 = torch.randn(2, 4, 5)
result = torch.bmm(input1, input2)