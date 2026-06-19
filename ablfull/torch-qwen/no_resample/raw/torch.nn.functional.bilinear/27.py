import torch

# Prepare valid input data
N = 2
Hin1 = 3
Hin2 = 4
out_features = 5
in1_features = 6
in2_features = 7

input1 = torch.randn(N, Hin1)
input2 = torch.randn(N, Hin2)
weight = torch.randn(out_features, in1_features, in2_features)
bias = torch.randn(out_features)

# Call the API
output = torch.nn.functional.bilinear(input1, input2, weight, bias)