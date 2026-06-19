
import torch
input_tensor = torch.tensor([(3 + 4j), (5 + 6j)], dtype=torch.complex64)
result = torch.view_as_real(input_tensor)
