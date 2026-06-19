import torch

# Prepare input data
N, Hin1, Hin2 = 2, 3, 4
in1_features, in2_features, out_features = 5, 6, 7

input1 = torch.randn(N, Hin1, in1_features)
input2 = torch.randn(N, Hin2, in2_features)
weight = torch.randn(out_features, in1_features, in2_features)
bias = torch.randn(out_features)

# Call the API
result = torch.nn.functional.bilinear(input1, input2, weight, bias)