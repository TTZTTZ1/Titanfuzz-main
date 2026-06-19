import torch
input1 = torch.randn(10, 3)
input2 = torch.randn(10, 4)
weight = torch.randn(5, 3, 4)
bias = torch.randn(5)
output = torch.nn.functional.bilinear(input1, input2, weight, bias)