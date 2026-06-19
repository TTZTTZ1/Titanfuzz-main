
import torch
N = 2
in1_features = 3
in2_features = 4
out_features = 5
Hin1 = Hin2 = 6
input1 = torch.randn(N, Hin1, in1_features)
input2 = torch.randn(N, Hin2, in2_features)
weight = torch.randn(out_features, in1_features, in2_features)
bias = torch.randn(out_features)
result = torch.nn.functional.bilinear(input1, input2, weight, bias)
