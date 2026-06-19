import torch

# Prepare input data
N, Hin1, Hin2 = 2, 3, 4
in1_features = 5
in2_features = 6
out_features = 7

input1 = torch.randn(N, Hin1, in1_features)
input2 = torch.randn(N, Hin2, in2_features)
weight = torch.randn(out_features, in1_features, in2_features)
bias = None  # Optional bias tensor

# Call the API
output = torch.nn.functional.bilinear(input1, input2, weight, bias)

print(output)