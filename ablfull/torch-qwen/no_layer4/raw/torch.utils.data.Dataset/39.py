import torch

class MyDataset(torch.utils.data.Dataset):
    def __init__(self, data):
        self.data = data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data[idx]

# Prepare valid input data
data = [torch.randn(3) for _ in range(5)]

# Call the API
dataset = MyDataset(data)