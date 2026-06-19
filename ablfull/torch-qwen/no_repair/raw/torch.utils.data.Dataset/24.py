import torch

class MyDataset(torch.utils.data.Dataset):
    def __init__(self):
        self.data = [1, 2, 3, 4, 5]

dataset = MyDataset()