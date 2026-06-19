import torch
input1 = torch.randn(2, 5)
input2 = torch.randn(2, 5)
output = torch.nn.functional.bilinear(input1, input2, weight=torch.randn(10, 5, 5), bias=None)