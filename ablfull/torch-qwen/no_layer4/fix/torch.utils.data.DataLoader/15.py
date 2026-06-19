import torch

class DummyDataset(torch.utils.data.Dataset):

    def __len__(self):
        return 10

    def __getitem__(self, idx):
        return torch.tensor([idx])
dataset = DummyDataset()
batch_size = 2
shuffle = False
num_workers = 0
pin_memory = False
drop_last = False
dataloader = torch.utils.data.DataLoader(dataset=dataset, batch_size=batch_size, shuffle=shuffle, num_workers=num_workers, pin_memory=pin_memory, drop_last=drop_last)