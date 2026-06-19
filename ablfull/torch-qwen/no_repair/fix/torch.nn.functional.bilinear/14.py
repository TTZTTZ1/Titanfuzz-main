
import torch
input1 = torch.randn(3, 4, requires_grad=True)
input2 = torch.randn(3, 5, requires_grad=True)
weight = torch.randn(6, 4, 5, requires_grad=True)
bias = torch.randn(6, requires_grad=True)
output = torch.nn.functional.bilinear(input1, input2, weight, bias)
