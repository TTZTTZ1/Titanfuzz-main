import torch

# Prepare valid input data
N, Hin1, Hin2 = 2, 3, 3
in1_features, in2_features, out_features = 4, 5, 6

input1 = torch.randn(N, *([Hin1] * 2), in1_features)
input2 = torch.randn(N, *([Hin2] * 2), in2_features)
weight = torch.randn(out_features, in1_features, in2_features)
bias = torch.randn(out_features)

# Call the API
output = torch.nn.functional.bilinear(input1, input2, weight, bias)