import torch

# Prepare valid input data
input1 = torch.randn(5, 10)
input2 = torch.randn(5, 15)
weight = torch.randn(20, 10, 15)
bias = torch.randn(20)

# Call the API
output = torch.nn.functional.bilinear(input1, input2, weight, bias)