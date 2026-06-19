import torch
input1 = torch.randn(2, 3, 5)
input2 = torch.randn(2, 3, 7)
weight = torch.randn(6, 5, 7)
bias = torch.randn(6)
output = torch.nn.functional.bilinear(input1, input2, weight, bias)