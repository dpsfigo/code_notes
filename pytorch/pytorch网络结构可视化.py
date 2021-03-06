# -*- coding: utf-8 -*-

import torch
from torchvision.models import AlexNet
from torchviz import make_dot

x=torch.rand(1,3,256,256)
model=AlexNet()
import hiddenlayer as h
vis_graph = h.build_graph(model, torch.zeros([1 ,3, 256, 256]))   # 获取绘制图像的对象
vis_graph.theme = h.graph.THEMES["blue"].copy()     # 指定主题颜色
vis_graph.save("./demo1.png")   # 保存图像的路径
# y=model(x)

# # 这三种方式都可以
# g = make_dot(y)
# # g=make_dot(y, params=dict(model.named_parameters()))
# #g = make_dot(y, params=dict(list(model.named_parameters()) + [('x', x)]))

# # 这两种方法都可以
# # g.view() # 会生成一个 Digraph.gv.pdf 的PDF文件
# g.render('espnet_model', view=False) # 会自动保存为一个 espnet.pdf，第二个参数为True,则会自动打开该PDF文件，为False则不打开

 
 
import torch
import tensorwatch as tw
from torchvision.models import AlexNet
#from lanenet_model.blocks import ESPNet_Encoder # 这是我自己定义的一个网络
 
# 其实就两句话
model=AlexNet()
tw.draw_model(model, [1, 3, 512, 256])