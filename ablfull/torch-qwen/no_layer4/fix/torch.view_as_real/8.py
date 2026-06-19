import torch
input_data = torch.tensor([[(1 + 2j), (3 + 4j)], [(5 + 6j), (7 + 8j)]], dtype=torch.complex64)
result = torch.view_as_real(input_data)