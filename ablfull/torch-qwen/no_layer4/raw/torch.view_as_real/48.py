import torch

# Create a complex tensor
input_tensor = torch.tensor([1+1j, 2+2j], dtype=torch.complex64)

# Call torch.view_as_real
result = torch.view_as_real(input_tensor)
print(result)