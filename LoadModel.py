'''
1. 保存整个网络结构信息和模型参数信息
torch.save(model_object, './model.pth')
直接加载即可使用：
model = torch.load('./model.pth')

2. 只保存网络的模型参数-推荐使用
torch.save(model_object.state_dict(), './params.pth')
加载则要先从本地网络模块导入网络，然后再加载参数：
from models import AgeModel
model = AgeModel()
model.load_state_dict(torch.load('./params.pth'))
'''

