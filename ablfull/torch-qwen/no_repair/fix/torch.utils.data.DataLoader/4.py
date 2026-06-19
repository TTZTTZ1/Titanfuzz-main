
import torch
dataset = torch.utils.data.TensorDataset(torch.randn(10, 3), torch.randint(0, 2, (10,)))
dataloader = torch.utils.data.DataLoader(dataset, batch_size=2, shuffle=False, num_workers=0, pin_memory=True, drop_last=False)
