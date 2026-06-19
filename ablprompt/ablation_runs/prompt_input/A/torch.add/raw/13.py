import torch

# Create two tensors
tensor1 = torch.tensor([1.0, 2.0, 3.0])
tensor2 = torch.tensor([4.0, 5.0, 6.0])

# Call the torch.add API to add the two tensors
result = torch.add(tensor1, tensor2)

print(result)