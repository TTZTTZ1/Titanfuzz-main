
import torch
data = torch.save({'key': 'value'}, 'test.pth')
result = torch.load('test.pth', map_location='cpu')
