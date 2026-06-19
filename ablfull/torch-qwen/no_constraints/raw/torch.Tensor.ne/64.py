import torch

# Prepare valid input data
tensor1 = torch.tensor([1, 2, 3])
tensor2 = torch.tensor([1, 4, 3])

# Call the API torch.Tensor.ne
result = tensor1.ne(tensor2)

print(result)