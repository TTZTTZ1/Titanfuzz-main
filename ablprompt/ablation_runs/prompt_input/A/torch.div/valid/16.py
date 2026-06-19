import torch

# Create two tensors
tensor1 = torch.tensor([2, 4, 6])
tensor2 = torch.tensor([1, 2, 3])

# Call torch.div to divide tensor1 by tensor2
result = torch.div(tensor1, tensor2)

print(result)