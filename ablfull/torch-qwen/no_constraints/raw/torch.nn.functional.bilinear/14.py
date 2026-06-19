import torch

input1 = torch.randn(2, 3)
input2 = torch.randn(4, 3)
weight = torch.randn(2, 4, 3)
bias = torch.randn(2)

output = torch.nn.functional.bilinear(input1, input2, weight, bias)