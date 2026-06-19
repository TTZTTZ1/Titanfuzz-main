import torch
from torch.nn.utils.prune import random_unstructured
module = torch.nn.Linear(10, 5)
parameters_to_prune = ('weight',)
pruning_amount = 0.2
random_unstructured(module, name=parameters_to_prune[0], amount=pruning_amount)