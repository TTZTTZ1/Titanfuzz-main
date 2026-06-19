import torch

# Prepare input data
input1 = torch.randn(2, 3, 4)
input2 = torch.randn(2, 5, 4)
weight = torch.randn(6, 4, 4)

# Call the API
output = torch.nn.functional.bilinear(input1, input2, weight)