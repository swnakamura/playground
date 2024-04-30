import torch

torch.nn.functional.grid_sample(torch.randn(1, 1, 3, 3), torch.randn(1, 3, 2, 2))
