import torch

class MyDataset(torch.utils.data.Dataset):
    def __init__(self, data):
        self.data = data

# Prepare valid input data
data = [1, 2, 3, 4, 5]

# Call the API
dataset = MyDataset(data)