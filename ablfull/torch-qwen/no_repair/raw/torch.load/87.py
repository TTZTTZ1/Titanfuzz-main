import torch

data = torch.load('path/to/file.pt', map_location=torch.device('cpu'))