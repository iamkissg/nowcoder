import numpy as np

import torch
import torch.nn as nn
import torch.optim as optim


class XOR(nn.Module):

    def __init__(self, input_size, output_size, nonlinear='sigmoid'):
        super(XOR, self).__init__()

        self.input_size = input_size
        self.output_size = output_size

        self.lin = nn.Linear(input_size, output_size)
        if nonlinear == 'relu':
            self.nonlinear = nn.ReLU()
        elif nonlinear == 'sigmoid':
            self.nonlinear = nn.Sigmoid()

    def forward(self, x):
        output = self.nonlinear(self.lin(x))
        return output


if __name__ == "__main__":
    ce = nn.CrossEntropyLoss()
    m = XOR(2, 1, 'sigmoid')
    optimizer = optim.Adam(m.parameters())

    X = torch.tensor([[0, 0], [0, 1], [1, 0], [1, 1]])
    Y = torch.tensor([0, 1, 1, 0])
    for x, y in zip(X, Y):
        m.zero_grad()

        pred = m(x)
        loss = ce(pred, y)
        loss.step()



