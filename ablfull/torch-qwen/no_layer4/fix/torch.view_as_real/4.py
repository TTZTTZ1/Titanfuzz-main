import torch
input_tensor = torch.tensor([(1 + 2j), (3 + 4j)], dtype=torch.complex64)
output = torch.view_as_real(input_tensor)