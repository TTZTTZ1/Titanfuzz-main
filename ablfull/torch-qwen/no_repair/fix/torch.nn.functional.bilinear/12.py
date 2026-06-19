
import torch
input1 = torch.randn(5, 10)
input2 = torch.randn(5, 10)
weight = torch.randn(20, 10, 10)
bias = torch.randn(20)
output = torch.nn.functional.bilinear(input1, input2, weight, bias)
