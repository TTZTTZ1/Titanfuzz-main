import torch

# Prepare input data
margin = 1.0
size_average = True
reduce = True
reduction = 'mean'

# Call the API
loss_fn = torch.nn.HingeEmbeddingLoss(margin=margin, size_average=size_average, reduce=reduce, reduction=reduction)