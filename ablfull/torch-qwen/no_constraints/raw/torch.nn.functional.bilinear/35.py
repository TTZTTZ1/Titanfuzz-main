import torch

# Prepare valid input data
input1 = torch.randn(2, 4)
input2 = torch.randn(2, 4)
weight = torch.randn(8, 4)

# Call the API
output = torch.nn.functional.bilinear(input1, input2, weight)