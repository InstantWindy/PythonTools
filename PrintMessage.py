'''
Print loss
'''
def print_current_losses(epoch, i, losses, t, t_data,log_name):
    message = '(epoch: %d, iters: %d, time: %.3f, data: %.3f) ' % (epoch, i, t, t_data)
    for k, v in losses.items():
        message += '%s: %.3f ' % (k, v)
    print(message)
    with open(log_name, "a") as log_file:
        log_file.write('%s\n' % message)