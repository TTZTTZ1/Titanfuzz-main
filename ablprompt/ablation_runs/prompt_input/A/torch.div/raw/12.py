import torch

# Create two tensors
tensor1 = torch.tensor([4.0, 2.0])
tensor2 = torch.tensor([2.0, 2.0])

# Call the torch.div function
result = torch.div(tensor1, tensor2)

# Print the result
print(result)