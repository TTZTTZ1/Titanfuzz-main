import torch

# Create two example tensors
tensor1 = torch.tensor([[1, 2], [3, 4]])
tensor2 = torch.tensor([[5, 6], [7, 8]])

# Call the torch.matmul function
result = torch.matmul(tensor1, tensor2)

print(result)