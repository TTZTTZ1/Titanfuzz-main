import torch
input1 = torch.randn(4, 5)
input2 = torch.randn(4, 6)
weight = torch.randn(7, 5, 6)
output = torch.nn.functional.bilinear(input1, input2, weight)