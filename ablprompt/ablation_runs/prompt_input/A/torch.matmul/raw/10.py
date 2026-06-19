import torch

# Create two tensors
tensor1 = torch.tensor([[1, 2], [3, 4]])
tensor2 = torch.tensor([[5, 6], [7, 8]])

# Call the API
result = torch.matmul(tensor1, tensor2)

print(result)