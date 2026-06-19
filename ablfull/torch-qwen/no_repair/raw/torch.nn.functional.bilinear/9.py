import torch

# Prepare input data
input1 = torch.randn(5, 3, 16)
input2 = torch.randn(5, 4, 16)
weight = torch.randn(8, 3, 4)
bias = torch.randn(8)

# Call the API
output = torch.nn.functional.bilinear(input1, input2, weight, bias)