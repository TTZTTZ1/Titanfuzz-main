
import torch
input1 = torch.randn(5, 3)
input2 = torch.randn(5, 4)
weight = torch.randn(6, 3, 4)
bias = torch.randn(6)
output = torch.nn.functional.bilinear(input1, input2, weight, bias)
