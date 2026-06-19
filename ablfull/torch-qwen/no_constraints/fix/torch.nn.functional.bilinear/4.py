import torch
input1 = torch.randn(5, 10)
input2 = torch.randn(5, 20)
weight = torch.randn(5, 10, 20)
output = torch.nn.functional.bilinear(input1, input2, weight)