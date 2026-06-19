import torch

# Create two tensors
tensor1 = torch.tensor([2.0, 3.0])
tensor2 = torch.tensor([3.0, 2.0])

# Call torch.pow
result = torch.pow(tensor1, tensor2)

print(result)