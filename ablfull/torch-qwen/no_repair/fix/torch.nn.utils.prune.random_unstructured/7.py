
import torch
import torch.nn.utils.prune as prune
module = torch.nn.Linear(10, 5)
name = 'weight'
amount = 0.5
prune.random_unstructured(module, name, amount)
