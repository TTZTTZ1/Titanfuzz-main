import torch

# Prepare input data
input1 = torch.randn(3, 5)
input2 = torch.randn(3, 4)

# Call the API
output = torch.nn.functional.bilinear(input1, input2, weight=torch.randn(5, 4), bias=None)