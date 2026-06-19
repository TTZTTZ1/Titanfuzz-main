import torch
from torch.utils.data import DataLoader, TensorDataset
dataset = TensorDataset(torch.randn(10, 3), torch.randint(0, 2, (10,)))
batch_size = 2
shuffle = True
sampler = None
batch_sampler = None
num_workers = 0
collate_fn = None
pin_memory = False
drop_last = False
timeout = 0
worker_init_fn = None
multiprocessing_context = None
generator = None
prefetch_factor = 2
persistent_workers = False
pin_memory_device = ''
in_order = True