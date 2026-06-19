import torch

# Create two random tensors
tensor1 = torch.randn(3, 4)
tensor2 = torch.randn(4, 5)

# Call the torch.matmul function
result = torch.matmul(tensor1, tensor2)

print(result)