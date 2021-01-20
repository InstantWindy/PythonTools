'''
plot loss figure
'''
import visdom
import numpy as np
def plot_current_losses(epoch, counter_ratio, opt, losses):
    '''
    :param epoch:
    :param counter_ratio:
        epoch_iter = 0
        epoch_iter += opt.batch_size
        dataset_size = len(opt.data_loader)
        counter_ratio = epoch_iter /dataset_size
    :param opt:
    :param losses: dictionary type, losses[name]=loss_value
    :return:
    '''
    display_id =1
    name ='model name'
    # if not hasattr(self, 'plot_data'):
    plot_data = {'X': [], 'Y': [], 'legend': list(losses.keys())}
    plot_data['X'].append(epoch + counter_ratio)
    plot_data['Y'].append([losses[k] for k in plot_data['legend']])
    # opt.display_server:http://localhost opt.display_port:8097
    vis = visdom.Visdom(server=opt.display_server, port=opt.display_port)
    vis.line(
        X=np.stack([np.array(plot_data['X'])] * len(plot_data['legend']), 1),
        Y=np.array(plot_data['Y']),
        opts={
            'title': name + ' loss over time',
            'legend': plot_data['legend'],
            'xlabel': 'epoch',
            'ylabel': 'loss'},
        win=display_id)  # display_id=1,window id of the web display

'''
draw curve
'''
import  os
import matplotlib.pyplot as plt

x_epoch = []
fig = plt.figure()
ax0 = fig.add_subplot(121, title="loss")
ax1 = fig.add_subplot(122, title="top1err")
y_loss = {} # loss history
y_loss['train'] = []
y_loss['val'] = []
y_err = {}
y_err['train'] = []
y_err['val'] = []

def draw_curve(current_epoch):
    name = 'fig'
    x_epoch.append(current_epoch)
    ax0.plot(x_epoch, y_loss['train'], 'bo-', label='train')
    ax0.plot(x_epoch, y_loss['val'], 'ro-', label='val')
    ax1.plot(x_epoch, y_err['train'], 'bo-', label='train')
    ax1.plot(x_epoch, y_err['val'], 'ro-', label='val')
    if current_epoch == 0:
        ax0.legend()
        ax1.legend()
    fig.savefig(os.path.join('./model',name,'train.jpg'))