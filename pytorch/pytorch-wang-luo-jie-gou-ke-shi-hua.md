# pytorch网络结构可视化

## 一，使用graphviz+torchviz来可视化模型

pip install graphviz \# 安装graphviz pip install git+[https://github.com/szagoruyko/pytorchviz](https://github.com/szagoruyko/pytorchviz) \# 通过git安装torchviz

```python
import torch
from torchvision.models import AlexNet
from torchviz import make_dot

 x=torch.rand(8,3,256,512)
 model=AlexNet()
 y=model(x)
```

## 二，通过tensorwatch+jupyter notebook来实现

