import matplotlib.pyplot as plt
from IPython.display import display, clear_output
from random import uniform


fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

servers = [[] for _ in range(5)]
servers_weigth = [round(uniform(0.1, 1), 1) for _ in range(5)]
servers_work_unused = [0 for _ in range(5)]

load = [round(uniform(0.1, 0.2), 1) for _ in range(50)] + \
       [round(uniform(0.3, 0.4), 1) for _ in range(50)] + \
       [round(uniform(0.6, 1), 1) for _ in range(50)] + \
       [round(uniform(0.1, 1), 1) for _ in range(50)]


def least_connection_weight_balance(request):
    E = sum([sum(server) for server in servers])
    if E == 0:
        E = 1
    servers_load = [(sum(server)/E)/servers_weigth[i] for i, server in enumerate(servers)]
    for i, server in enumerate(servers):
        servers_load.append(sum(server)/E/servers_weigth[i])
    lowest_loaded_server = servers_load.index(min(servers_load))
    servers[lowest_loaded_server].append(request)


def calculate_servers_load():
    for i, server in enumerate(servers):
        if server != []:
            servers_work_unused[i] += servers_weigth[i]
        while True:
            if server != [] and server[-1] <= servers_work_unused[i]:
                servers_work_unused[i] -= server.pop(-1)
            else:
                break 
    

for z in range(0, 200):
        ax.cla()
        plt.title(str(z/2) + f" s / Долг \nМощности серверов - {' '.join([str(x) for x in servers_weigth])}")
        if z % 4 == 0 and z // 4 <= 2 and z != 0 :
            for i in range(25):
                least_connection_weight_balance(load[25*(z//4 - 1) + i])
                plt.title(str(z/2) + " s / Долг (Мелкие задачи)")
        elif z % 4 == 0 and z // 4 <= 4 and z // 4 >= 3 and z != 0 :
            for i in range(25):
                least_connection_weight_balance(load[25*(z//4 - 2) + i])
                plt.title(str(z/2) + " s / Долг (Средние задачи)")
        elif z % 4 == 0 and z // 4 <= 7 and z // 4 >= 6 and z != 0 :
            for i in range(25):
                least_connection_weight_balance(load[25*(z//4 - 4) + i])
                plt.title(str(z/2) + " s / Долг (Высокие задачи)")
        elif z % 4 == 0 and z // 4 <= 11 and z // 4 >= 10 and z != 0 :
            for i in range(25):
                least_connection_weight_balance(load[25*(z//4 - 8) + i])
                plt.title(str(z/2) + " s / Долг (Смешанные задачи)")
        else: 
            calculate_servers_load()
        plt.bar(list(range(1, 6)), [sum(server) for server in servers], width=1, bottom=None, align='center')
        display(fig)
        clear_output(wait = True)
        plt.pause(0.5)