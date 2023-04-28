import torch
import torch.nn as nn
import torch.optim as optim


class Trainer:
    def __init__(self, model, lr, gamma):
        self.lr = lr
        self.gamma = gamma
        self.model = model
        self.optimer = optim.Adam(model.parameters(), lr=self.lr)
        self.criterion = nn.MSELoss()
        for i in self.model.parameters():
            print(i.is_cuda)

    def train_step(self, state, action, reward, next_state, done):
        state = torch.tensor(state, dtype=torch.float).cuda()
        next_state = torch.tensor(next_state, dtype=torch.float).cuda()
        action = torch.tensor(action, dtype=torch.long).cuda()
        reward = torch.tensor(reward, dtype=torch.float).cuda()

        if len(state.shape) == 1:  # only one parameter to train ,
            # Hence convert to tuple of shape (1, x)
            state = torch.unsqueeze(state, 0).cuda()
            next_state = torch.unsqueeze(next_state, 0).cuda()
            action = torch.unsqueeze(action, 0).cuda()
            reward = torch.unsqueeze(reward, 0).cuda()
            done = (done, )

        # 1. Predicted Q value with current state
        pred = self.model(state).cuda()
        target = pred.clone().cuda()
        for idx in range(len(done)):
            Q_new = reward[idx]
            if not done[idx]:
                Q_new = reward[idx] + self.gamma * torch.max(self.model(next_state[idx])).cuda()
            target[idx][torch.argmax(action).item()] = Q_new
        # 2. Q_new = reward + gamma * max(next_predicted Qvalue)
        # -> only do this if not done
        # pred.clone()
        # preds[argmax(action)] = Q_new
        self.optimer.zero_grad()
        loss = self.criterion(target, pred)
        loss.backward()

        self.optimer.step()
