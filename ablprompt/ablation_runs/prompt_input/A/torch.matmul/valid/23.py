import torch

# Create two random tensors
tensor1 = torch.randn(2, 3)
tensor2 = torch.randn(3, 4)

# Call torch.matmul to multiply the tensors
result = torch.matmul(tensor1, tensor2)

print(result)