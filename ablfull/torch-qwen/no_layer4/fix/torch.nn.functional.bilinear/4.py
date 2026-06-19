import torch
input1 = torch.randn(5, 3, 6)
input2 = torch.randn(5, 3, 7)
weight = torch.randn(8, 6, 7)
bias = torch.randn(8)
output = torch.nn.functional.bilinear(input1, input2, weight, bias)