import torch
input_tensor = torch.tensor([[[[(1 + 2j)], [(3 + 4j)]], [[(5 + 6j)], [(7 + 8j)]]]])
result = torch.view_as_real(input_tensor)
print(result)