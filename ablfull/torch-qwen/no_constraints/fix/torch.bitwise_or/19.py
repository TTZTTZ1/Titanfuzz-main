import torch
input_tensor1 = torch.tensor([12], dtype=torch.uint8)
input_tensor2 = torch.tensor([10], dtype=torch.uint8)
result = torch.bitwise_or(input_tensor1, input_tensor2)