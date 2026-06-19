import torch

# Create two tensors
tensor1 = torch.tensor([2, 3, 4])
tensor2 = torch.tensor([1, 1, 1])

# Call the torch.sub API to subtract tensor2 from tensor1
result = torch.sub(tensor1, tensor2)

print(result)