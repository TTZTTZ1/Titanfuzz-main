import torch
input1 = torch.randn(3, 5)
input2 = torch.randn(3, 6)
weight = torch.randn(7, 5, 6)
bias = torch.randn(7)
output = torch.nn.functional.bilinear(input1, input2, weight, bias)