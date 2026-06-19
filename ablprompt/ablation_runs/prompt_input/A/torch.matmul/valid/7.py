import torch

# Create two random tensors
tensor1 = torch.randn(3, 4)
tensor2 = torch.randn(4, 5)

# Call torch.matmul to multiply the tensors
result = torch.matmul(tensor1, tensor2)

# Print the result
print(result)