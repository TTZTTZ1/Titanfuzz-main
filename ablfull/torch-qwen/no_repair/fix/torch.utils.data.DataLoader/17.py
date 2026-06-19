
import torch

class SimpleDataset(torch.utils.data.Dataset):

    def __init__(self, data):
        self.data = data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data[idx]
data = [i for i in range(10)]
dataset = SimpleDataset(data)
dataloader = torch.utils.data.DataLoader(dataset=dataset, batch_size=2, shuffle=False, num_workers=0, pin_memory=True)
