import torch

# Prepare input data
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

# Ensure constraints are met
assert input1.shape[:-1] == input2.shape[:-1]
assert input1.shape[-1] == weight.shape[1]
assert input2.shape[-1] == weight.shape[2]
assert bias is None or bias.shape == (weight.shape[0],)

# Call the API
output = torch.nn.functional.bilinear(input1, input2, weight, bias)