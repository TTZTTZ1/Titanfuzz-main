import torch

class MyDataset(torch.utils.data.Dataset):
    def __init__(self, data):
        self.data = data
    
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, idx):
        return self.data[idx]

# Prepare valid input data
data = [torch.randn(3, 256, 256) for _ in range(10)]

# Create an instance of the dataset
dataset = MyDataset(data)

# Call the API
print(dataset[0])