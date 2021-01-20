'''
optimizer way 1
'''
from  torchvision import models
import torch.optim as optim
model = models.resnet50()
lr =0.001
ignored_params = list(map(id, model.classifier.parameters()))
base_params = filter(lambda p: id(p) not in ignored_params, model.parameters())
optimizer_ft = optim.SGD([
    {'params': base_params, 'lr': 0.1 * lr},
    {'params': model.classifier.parameters(), 'lr': lr}
], weight_decay=5e-4, momentum=0.9, nesterov=True)


'''
optimizer way 2
'''
ignored_params = list(map(id, model.model.fc.parameters()))
ignored_params += (list(map(id, model.classifier0.parameters()))
                   + list(map(id, model.classifier1.parameters()))
                   + list(map(id, model.classifier2.parameters()))
                   + list(map(id, model.classifier3.parameters()))
                   + list(map(id, model.classifier4.parameters()))
                   + list(map(id, model.classifier5.parameters()))
                   # +list(map(id, model.classifier6.parameters() ))
                   # +list(map(id, model.classifier7.parameters() ))
                   )
base_params = filter(lambda p: id(p) not in ignored_params, model.parameters())
optimizer_ft = optim.SGD([
    {'params': base_params, 'lr': 0.1 * lr},
    {'params': model.model.fc.parameters(), 'lr': lr},
    {'params': model.classifier0.parameters(), 'lr': lr},
    {'params': model.classifier1.parameters(), 'lr': lr},
    {'params': model.classifier2.parameters(), 'lr': lr},
    {'params': model.classifier3.parameters(), 'lr': lr},
    {'params': model.classifier4.parameters(), 'lr': lr},
    {'params': model.classifier5.parameters(), 'lr': lr},
    # {'params': model.classifier6.parameters(), 'lr': 0.01},
    # {'params': model.classifier7.parameters(), 'lr': 0.01}

], weight_decay=5e-4, momentum=0.9, nesterov=True)