import torch

# Create two tensors
tensor1 = torch.tensor([1.0, 2.0, 3.0])
tensor2 = torch.tensor([4.0, 5.0, 6.0])

# Call torch.mul to multiply the two tensors element-wise
result = torch.mul(tensor1, tensor2)

print(result)