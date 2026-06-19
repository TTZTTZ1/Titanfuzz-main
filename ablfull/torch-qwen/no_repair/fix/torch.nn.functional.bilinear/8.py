
import torch
input1 = torch.randn(3, 5)
input2 = torch.randn(3, 7)
weight = torch.randn(4, 5, 7)
output = torch.nn.functional.bilinear(input1, input2, weight, bias=None)
