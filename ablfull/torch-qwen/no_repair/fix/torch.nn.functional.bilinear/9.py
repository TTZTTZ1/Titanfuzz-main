
import torch
input1 = torch.randn(2, 5)
input2 = torch.randn(2, 3)
weight = torch.randn(4, 5, 3)
bias = torch.randn(4)
output = torch.nn.functional.bilinear(input1, input2, weight, bias)
