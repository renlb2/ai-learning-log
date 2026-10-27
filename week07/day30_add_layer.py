import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

# 1. 准备数据
# transforms.ToTensor() 会把图片从 0-255 转成 0-1 之间的 Tensor
transform = transforms.Compose([transforms.ToTensor()])

# 下载训练集和测试集到当前目录下的 data 文件夹
train_dataset = datasets.MNIST(root='./data', train=True, download=True, transform=transform)
test_dataset = datasets.MNIST(root='./data', train=False, download=True, transform=transform)

# DataLoader 负责把数据分批次（batch）喂给模型，每批 64 张图
train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=1000, shuffle=False)

# 2. 定义神经网络
class SimpleNet(nn.Module):
    def __init__(self):
        super().__init__()
        # 输入层 784 (28*28像素) -> 隐藏层 128 -> 输出层 10 (0-9数字)
        self.fc1 = nn.Linear(784, 256)
        self.relu = nn.ReLU()  # 激活函数
        self.fc_extra = nn.Linear(256,128)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(128, 10)

    def forward(self, x):
        x = x.view(-1, 784)   # 把 28x28 的图拉平成 784 的向量
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc_extra(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x

model = SimpleNet()

# 3. 定义损失函数（算错得多离谱）和优化器（怎么改错）
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.01) # 随机梯度下降，学习率 0.01

# 4. 开始训练（这就是深度学习核心的“训练循环”）
epochs = 5
for epoch in range(epochs):
    model.train() # 设置为训练模式
    for batch_idx, (data, target) in enumerate(train_loader):
        # --- 固定的 5 步 ---
        optimizer.zero_grad()          # 第1步：清空上一步残留的梯度
        output = model(data)           # 第2步：前向传播（模型猜答案）
        loss = criterion(output, target) # 第3步：算损失（猜错了多少）
        loss.backward()                # 第4步：反向传播（算谁的锅）
        optimizer.step()               # 第5步：更新参数（大家改一下）
        # -------------------
    
    print(f"Epoch {epoch+1} 训练完成。")

# 5. 评估模型
model.eval() # 设置为评估模式
correct = 0
total = 0
with torch.no_grad(): # 评估时不计算梯度，省内存
    for data, target in test_loader:
        output = model(data)
        # 取概率最大的那个数字作为预测结果
        _, predicted = torch.max(output.data, 1)
        total += target.size(0)
        correct += (predicted == target).sum().item()

print(f"测试集准确率: {100 * correct / total:.2f}%")
