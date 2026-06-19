import torch
input_matrix = torch.randn(3, 3)
while (torch.abs(torch.det(input_matrix)) < 1e-06):
    input_matrix = torch.randn(3, 3)
result = torch.linalg.inv(input_matrix)