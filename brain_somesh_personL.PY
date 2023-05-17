import torch.nn as nn
#pip install torch

class neuralNetwork(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        super(neuralNetwork, self).__init__()
        self.11 = nn.Linear(input_size, hidden_size)
        self.12 = nn.Linear(hidden_size, hidden_size)
        self.13 = nn.Linear(hidden_size, num_classes)
        self.relu = nn.ReLU()
        
    def forward(self,x):
        out = self.11(x)
        out = self.relu(out)
        out = self.12(out)
        out = self.relu(out)
        out = self.13(out)
        return out
