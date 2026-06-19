import torch

# Prepare input data
N = 3
Hin1 = 5
Hin2 = 7
out_features = 9

input1 = torch.randn(N, Hin1)
input2 = torch.randn(N, Hin2)
weight = torch.randn(out_features, Hin1, Hin2)

# Call the API
output = torch.nn.functional.bilinear(input1, input2, weight)