import torch

# Task 2: Generate input data - No specific constraints given, so we use default values
class MyDataset(torch.utils.data.Dataset):
    def __init__(self):
        self.data = torch.tensor([1.0, 2.0, 3.0])

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data[idx]

# Task 3: Call the API torch.utils.data.Dataset
dataset = MyDataset()