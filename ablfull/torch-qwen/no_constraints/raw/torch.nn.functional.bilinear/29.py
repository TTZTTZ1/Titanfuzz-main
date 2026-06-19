import torch

# Prepare input data
input1 = torch.randn(3, 4)
input2 = torch.randn(3, 5)

# Call the API
output = torch.nn.functional.bilinear(input1, input2, weight=torch.randn(4, 5), bias=None)