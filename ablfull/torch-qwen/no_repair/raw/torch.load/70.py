import torch

data = torch.load('path_to_your_file.pt', map_location=torch.device('cpu'))