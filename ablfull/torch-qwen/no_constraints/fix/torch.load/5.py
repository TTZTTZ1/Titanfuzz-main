import torch
dummy_tensor = torch.tensor([1.0, 2.0, 3.0])
with open('temp.pth', 'wb') as f:
    torch.save(dummy_tensor, f)
result = torch.load('temp.pth')
print(result)