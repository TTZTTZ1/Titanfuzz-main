import torch
input1 = torch.randn(10, 5)
input2 = torch.randn(10, 7)
weight = torch.randn(3, 5, 7)
bias = torch.randn(3)
output = torch.nn.functional.bilinear(input1, input2, weight, bias=bias)