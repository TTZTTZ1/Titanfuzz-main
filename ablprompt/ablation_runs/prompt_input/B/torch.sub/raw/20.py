import torch

a = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)
b = torch.tensor([[5, 6], [7, 8]], dtype=torch.float32)
alpha = 2
result = torch.sub(a, b, alpha=alpha)
print(result)  # Output: tensor([[-9., -10.],
                #         [-14., -16.]])