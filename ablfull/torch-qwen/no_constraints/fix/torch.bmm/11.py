import torch
input1 = torch.randn(10, 3, 4)
input2 = torch.randn(10, 4, 5)
output = torch.bmm(input1, input2)
print(output.shape)