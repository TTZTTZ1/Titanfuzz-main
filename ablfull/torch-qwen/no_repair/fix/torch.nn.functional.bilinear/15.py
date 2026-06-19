
import torch
input1 = torch.randn(5, 3, 4)
input2 = torch.randn(5, 3, 6)
weight = torch.randn(7, 4, 6)
bias = None
output = torch.nn.functional.bilinear(input1, input2, weight, bias)
