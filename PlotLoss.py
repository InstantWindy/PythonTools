
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

import numpy as np
def plot_loss(apath, epoch,loss,log):
    axis = np.linspace(1, epoch, epoch)
    for i, l in enumerate(loss):
        label = '{} Loss'.format(l['type'])
        fig = plt.figure()
        plt.title(label)
        plt.plot(axis, log[:, i].numpy(), label=label)
        plt.legend()
        plt.xlabel('Epochs')
        plt.ylabel('Loss')
        plt.grid(True)
        plt.savefig('{}/loss_{}.pdf'.format(apath, l['type']))
        plt.close(fig)
