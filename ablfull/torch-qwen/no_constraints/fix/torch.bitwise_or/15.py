import torch
input1 = torch.tensor([1, 0, 1, 0], dtype=torch.uint8)
input2 = torch.tensor([1, 1, 0, 0], dtype=torch.uint8)
result = torch.bitwise_or(input1, input2)
print(result)