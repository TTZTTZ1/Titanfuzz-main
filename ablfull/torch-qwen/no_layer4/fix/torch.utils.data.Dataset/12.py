import torch

class MyDataset(torch.utils.data.Dataset):

    def __init__(self, data):
        self.data = data
data = [1, 2, 3, 4, 5]
dataset = MyDataset(data)