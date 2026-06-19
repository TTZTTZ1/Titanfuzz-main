import torch
data = torch.tensor([1.0, 2.0, 3.0, 4.0, 5.0])
(std, mean) = torch.std_mean(data)