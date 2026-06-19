
import torch

class DummyDataset(torch.utils.data.Dataset):

    def __getitem__(self, index):
        return torch.tensor([index])

    def __len__(self):
        return 10
dataset = DummyDataset()
dataloader = torch.utils.data.DataLoader(dataset, batch_size=2, shuffle=False, num_workers=0, pin_memory=True, drop_last=False)
