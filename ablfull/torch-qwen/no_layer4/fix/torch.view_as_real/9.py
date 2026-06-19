import torch
input_tensor = torch.tensor([(1 + 1j), (2 + 2j)], dtype=torch.complex64)
result = torch.view_as_real(input_tensor)
print(result)