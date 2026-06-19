import torch

# Create a complex tensor
input_tensor = torch.tensor([1+1j, 2+2j], dtype=torch.complex64)

# View the tensor as real numbers
result = torch.view_as_real(input_tensor)
print(result)