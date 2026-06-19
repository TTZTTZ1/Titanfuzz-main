import torch
input1 = torch.randn(3, 4)
input2 = torch.randn(3, 5)
output = torch.nn.functional.bilinear(input1, input2, weight=torch.randn(6, 4, 5), bias=None)