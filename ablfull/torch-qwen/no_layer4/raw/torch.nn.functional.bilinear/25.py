import torch

# Prepare input data
input1 = torch.randn(2, 3, 4)
input2 = torch.randn(2, 3, 5)
weight = torch.randn(6, 4, 5)
bias = torch.randn(6)

# Call the API
output = torch.nn.functional.bilinear(input1, input2, weight, bias)