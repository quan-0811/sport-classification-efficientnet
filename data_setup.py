import torchvision
from torch.utils.data import DataLoader
import os

def create_dataloaders(train_dir: str, valid_dir: str, test_dir: str, batch_size: int, transform):

    train_dataset = torchvision.datasets.ImageFolder(root=train_dir,
                                                     transform=transform)
    valid_dataset = torchvision.datasets.ImageFolder(root=valid_dir,
                                                     transform=transform)
    test_dataset = torchvision.datasets.ImageFolder(root=test_dir,
                                                    transform=transform)

    train_dataloader = DataLoader(dataset=train_dataset,
                                  batch_size=batch_size,
                                  num_workers=os.cpu_count(),
                                  shuffle=True,
                                  pin_memory=True)
    valid_dataloader = DataLoader(dataset=valid_dataset,
                                  batch_size=batch_size,
                                  num_workers=os.cpu_count(),
                                  shuffle=False)
    test_dataloader = DataLoader(dataset=test_dataset,
                                 batch_size=batch_size,
                                 num_workers=os.cpu_count(),
                                 shuffle=False,
                                 pin_memory=True)

    return train_dataloader, valid_dataloader, test_dataloader, train_dataset.classes