
import torch
x = torch.tensor(2.0, requires_grad=True)
y = (x ** 2)
enabled = torch.is_grad_enabled()
print(f'Gradient enabled: {enabled}')
with torch.no_grad():
    z = (x ** 2)
    print(f'Gradient enabled within context manager: {torch.is_grad_enabled()}')
