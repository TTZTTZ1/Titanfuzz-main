import torch

class MyDataset(torch.utils.data.Dataset):
    def __init__(self, data):
        self.data = data
    
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, idx):
        return self.data[idx]

# Example usage
data = [1, 2, 3, 4, 5]
dataset = MyDataset(data)
print(dataset[0])