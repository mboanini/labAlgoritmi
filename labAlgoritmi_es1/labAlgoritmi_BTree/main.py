import random
import numpy as np
import matplotlib.pyplot as plt
import timeit
import os

from ABR import *
from BTree import *


def drawTable(columns: list, headers: tuple, tablename: str):
    fig, ax = plt.subplots(figsize=(9, 18))

    data = np.stack(tuple(columns), axis=1)

    ax.axis('off')
    table = ax.table(cellText=data, colLabels=headers, loc='center', cellLoc='center')
    table.auto_set_column_width(col=list(range(len(columns))))
    table.scale(1, 1.5)

    for cell in table._cells:
        if table[cell].get_text().get_text() in headers:
            table[cell].set_facecolor("#c1d6ff")
            table[cell].set_text_props(weight='bold')
        elif cell[0] % 2 == 0:
            table[cell].set_facecolor("#deebff")

    fig.savefig(f"./tables/{tablename}.png", bbox_inches='tight')


def drawPlot_time(x, y, title: str, plotname: str):
    fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
    ax.plot(x, y, label='ABR')  # Plot some data on the axes.
    ax.set_xlabel('Numero elementi')  # Add an x-label to the axes.
    ax.set_ylabel('Tempo [ms]')  # Add a y-label to the axes.
    ax.set_title(title)  # Add a title to the axes.
    plt.show()
    fig.savefig(f"./plots/{plotname}.png", bbox_inches='tight')


def drawPlot_node(x, y, title: str, plotname: str):
    fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
    ax.plot(x, y, label='ABR')
    ax.set_xlabel('Numero elementi')
    ax.set_ylabel('Numero nodi')
    ax.set_title(title)
    plt.show()
    fig.savefig(f"./plots/{plotname}.png", bbox_inches='tight')


def draw3Plot_time(x, y1, y2, y3, title: str, plotname: str):
    fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
    ax.plot(x, y1, 'c', label='B-Albero(t=t1)')
    ax.plot(x, y2, 'm', label='B-Albero(t=t2)')
    ax.plot(x, y3, 'r', label='B-Albero(t=t3)')
    ax.set_xlabel('Numero elementi')
    ax.set_ylabel('Tempo [ms]')
    ax.set_title(title)
    ax.legend()
    plt.show()
    fig.savefig(f"./plots/{plotname}.png", bbox_inches='tight')


def draw3Plot_node(x, y1, y2, y3, title: str, plotname: str):
    fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
    ax.plot(x, y1, 'c', label='B-Albero(t=t1)')
    ax.plot(x, y2, 'm', label='B-Albero(t=t2)')
    ax.plot(x, y3, 'r', label='B-Albero(t=t3)')
    ax.set_xlabel('Numero elementi')
    ax.set_ylabel('Numero nodi')
    ax.set_title(title)
    ax.legend()
    plt.show()
    fig.savefig(f"./plots/{plotname}.png", bbox_inches='tight')


def draw4Plot_time(x, y0, y1, y2, y3, title: str, plotname: str):
    fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
    ax.plot(x, y0, label='ABR')
    ax.plot(x, y1, 'c', label='B-Albero(t=t1)')
    ax.plot(x, y2, 'm', label='B-Albero(t=t2)')
    ax.plot(x, y3, 'r', label='B-Albero(t=t3)')
    ax.set_xlabel('Numero elementi')
    ax.set_ylabel('Tempo [ms]')
    ax.set_title(title)
    ax.legend()
    plt.show()
    fig.savefig(f"./plots/{plotname}.png", bbox_inches='tight')


def draw4Plot_node(x, y0, y1, y2, y3, title: str, plotname: str):
    fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
    ax.plot(x, y0, label='ABR')
    ax.plot(x, y1, 'c', label='B-Albero(t=t1)')
    ax.plot(x, y2, 'm', label='B-Albero(t=t2)')
    ax.plot(x, y3, 'r', label='B-Albero(t=t3)')
    ax.set_xlabel('Numero elementi')
    ax.set_ylabel('Numero nodi')
    ax.set_title(title)
    ax.legend()
    plt.show()
    fig.savefig(f"./plots/{plotname}.png", bbox_inches='tight')


def main():
    result_time_insert_abr = []
    result_time_insert_btree1 = []
    result_time_insert_btree2 = []
    result_time_insert_btree3 = []
    result_time_search_abr = []
    result_time_search_btree1 = []
    result_time_search_btree2 = []
    result_time_search_btree3 = []

    result_node_insert_abr = []
    result_node_insert_btree1 = []
    result_node_insert_btree2 = []
    result_node_insert_btree3 = []
    result_node_search_abr = []
    result_node_search_btree1 = []
    result_node_search_btree2 = []
    result_node_search_btree3 = []

    for it in range(num_iter_test):
        result_time_insert_abr_partial = []
        result_time_insert_btree1_partial = []
        result_time_insert_btree2_partial = []
        result_time_insert_btree3_partial = []
        result_time_search_abr_partial = []
        result_time_search_btree1_partial = []
        result_time_search_btree2_partial = []
        result_time_search_btree3_partial = []

        result_node_insert_abr_partial = []
        result_node_insert_btree1_partial = []
        result_node_insert_btree2_partial = []
        result_node_insert_btree3_partial = []
        result_node_search_abr_partial = []
        result_node_search_btree1_partial = []
        result_node_search_btree2_partial = []
        result_node_search_btree3_partial = []

        t1 = 250
        t2 = 500
        t3 = 2000
        array_test = np.random.randint(0, 1000, 10000)
        my_btree1 = BTree(t1)
        my_btree2 = BTree(t2)
        my_btree3 = BTree(t3)
        my_tree = ABR()
        values_inserted = []

        block_size = 200

        for j in range(0, len(array_test), block_size):
            # insertion test in abr
            start_time = timeit.default_timer()
            for k in range(0, block_size):
                new_node = ABRNode(array_test[j + k])
                my_tree.ABR_insert(new_node)
                values_inserted.append(array_test[j + k])
            end_time = timeit.default_timer()
            result_time_insert_abr_partial.append((end_time - start_time) * 1000)
            result_node_insert_abr_partial.append(my_tree.get_node_read() + my_tree.get_node_written())
            my_tree.node_read = 0
            my_tree.node_written = 0

            # insertion test in btree with t = t1
            start_time = timeit.default_timer()
            for k in range(0, block_size):
                my_btree1.btree_insert(array_test[j + k])
            end_time = timeit.default_timer()
            result_time_insert_btree1_partial.append((end_time - start_time) * 1000)
            result_node_insert_btree1_partial.append(my_btree1.get_node_read() + my_btree1.get_node_written())
            my_btree1.node_read = 0
            my_btree1.node_written = 0

            # insertion test in btree with t = t2
            start_time = timeit.default_timer()
            for k in range(0, block_size):
                my_btree2.btree_insert(array_test[j + k])
            end_time = timeit.default_timer()
            result_time_insert_btree2_partial.append((end_time - start_time) * 1000)
            result_node_insert_btree2_partial.append(my_btree2.get_node_read() + my_btree2.get_node_written())
            my_btree2.node_read = 0
            my_btree2.node_written = 0

            # insertion test in btree with t = t3
            start_time = timeit.default_timer()
            for k in range(0, block_size):
                my_btree3.btree_insert(array_test[j + k])
            end_time = timeit.default_timer()
            result_time_insert_btree3_partial.append((end_time - start_time) * 1000)
            result_node_insert_btree3_partial.append(my_btree3.get_node_read() + my_btree3.get_node_written())
            my_btree3.node_read = 0
            my_btree3.node_written = 0

            # search test in abr
            start_time = timeit.default_timer()
            for k in range(0, block_size):
                my_tree.ABR_search(random.choice(values_inserted))
            end_time = timeit.default_timer()
            result_time_search_abr_partial.append((end_time - start_time) * 1000)
            result_node_search_abr_partial.append(my_tree.get_node_read() + my_tree.get_node_written())
            my_tree.node_read = 0
            my_tree.node_written = 0

            # search test in btree with t = t1
            start_time = timeit.default_timer()
            for k in range(0, block_size):
                my_btree1.btree_search(random.choice(values_inserted))
            end_time = timeit.default_timer()
            result_time_search_btree1_partial.append((end_time - start_time) * 1000)
            result_node_search_btree1_partial.append(my_btree1.get_node_read() + my_btree1.get_node_written())
            my_tree.node_read = 0
            my_tree.node_written = 0

            # search test in btree with t = t2
            start_time = timeit.default_timer()
            for k in range(0, block_size):
                my_btree2.btree_search(random.choice(values_inserted))
            end_time = timeit.default_timer()
            result_time_search_btree2_partial.append((end_time - start_time) * 1000)
            result_node_search_btree2_partial.append(my_btree2.get_node_read() + my_btree2.get_node_written())
            my_tree.node_read = 0
            my_tree.node_written = 0

            # search test in btree with t = t3
            start_time = timeit.default_timer()
            for k in range(0, block_size):
                my_btree3.btree_search(random.choice(values_inserted))
            end_time = timeit.default_timer()
            result_time_search_btree3_partial.append((end_time - start_time) * 1000)
            result_node_search_btree3_partial.append(my_btree3.get_node_read() + my_btree3.get_node_written())
            my_tree.node_read = 0
            my_tree.node_written = 0

        # inserting values into arrays and calculating the average
        if it == 0:
            for i in range(0, len(result_time_insert_abr_partial)):
                result_time_insert_abr.append(result_time_insert_abr_partial[i])
                result_node_insert_abr.append(result_node_insert_abr_partial[i])
                result_time_insert_btree1.append(result_time_insert_btree1_partial[i])
                result_node_insert_btree1.append(result_node_insert_btree1_partial[i])
                result_time_insert_btree2.append(result_time_insert_btree2_partial[i])
                result_node_insert_btree2.append(result_node_insert_btree2_partial[i])
                result_time_insert_btree3.append(result_time_insert_btree3_partial[i])
                result_node_insert_btree3.append(result_node_insert_btree3_partial[i])

                result_time_search_abr.append(result_time_search_abr_partial[i])
                result_node_search_abr.append(result_node_search_abr_partial[i])
                result_time_search_btree1.append(result_time_search_btree1_partial[i])
                result_node_search_btree1.append(result_node_search_btree1_partial[i])
                result_time_search_btree2.append(result_time_search_btree2_partial[i])
                result_node_search_btree2.append(result_node_search_btree2_partial[i])
                result_time_search_btree3.append(result_time_search_btree3_partial[i])
                result_node_search_btree3.append(result_node_search_btree3_partial[i])
        else:
            for i in range(0, len(result_time_insert_abr)):
                result_time_insert_abr[i] += result_time_insert_abr_partial[i]
                result_node_insert_abr[i] += result_node_insert_abr_partial[i]
                result_time_insert_btree1[i] += result_time_insert_btree1_partial[i]
                result_node_insert_btree1[i] += result_node_insert_btree1_partial[i]
                result_time_insert_btree2[i] += result_time_insert_btree2_partial[i]
                result_node_insert_btree2[i] += result_node_insert_btree2_partial[i]
                result_time_insert_btree3[i] += result_time_insert_btree3_partial[i]
                result_node_insert_btree3[i] += result_node_insert_btree3_partial[i]

                result_time_search_abr[i] += result_time_search_abr_partial[i]
                result_node_search_abr[i] += result_node_search_abr_partial[i]
                result_time_search_btree1[i] += result_time_search_btree1_partial[i]
                result_node_search_btree1[i] += result_node_search_btree1_partial[i]
                result_time_search_btree2[i] += result_time_search_btree2_partial[i]
                result_node_search_btree2[i] += result_node_search_btree2_partial[i]
                result_time_search_btree3[i] += result_time_search_btree3_partial[i]
                result_node_search_btree3[i] += result_node_search_btree3_partial[i]

    for i in range(0, len(result_time_insert_abr)):
        result_time_insert_abr[i] = result_time_insert_abr[i] / num_iter_test
        result_node_insert_abr[i] = result_node_insert_abr[i] / num_iter_test
        result_time_insert_btree1[i] = result_time_insert_btree1[i] / num_iter_test
        result_node_insert_btree1[i] = result_node_insert_btree1[i] / num_iter_test
        result_time_insert_btree2[i] = result_time_insert_btree2[i] / num_iter_test
        result_node_insert_btree2[i] = result_node_insert_btree2[i] / num_iter_test
        result_time_insert_btree3[i] = result_time_insert_btree3[i] / num_iter_test
        result_node_insert_btree3[i] = result_node_insert_btree3[i] / num_iter_test

        result_time_search_abr[i] = result_time_search_abr[i] / num_iter_test
        result_node_search_abr[i] = result_node_search_abr[i] / num_iter_test
        result_time_search_btree1[i] = result_time_search_btree1[i] / num_iter_test
        result_node_search_btree1[i] = result_node_search_btree1[i] / num_iter_test
        result_time_search_btree2[i] = result_time_search_btree2[i] / num_iter_test
        result_node_search_btree2[i] = result_node_search_btree2[i] / num_iter_test
        result_time_search_btree3[i] = result_time_search_btree3[i] / num_iter_test
        result_node_search_btree3[i] = result_node_search_btree3[i] / num_iter_test

    print("Tempi inserimento ABR: ", result_time_insert_abr)
    print("Tempi inserimento B-albero t=t1: ", result_time_insert_btree1)
    print("Tempi inserimento B-albero t=t2: ", result_time_insert_btree2)
    print("Tempi inserimento B-albero t=t3: ", result_time_insert_btree3)
    print("------")
    print("Tempi ricerca ABR: ", result_time_search_abr)
    print("Tempi ricerca B-albero con t=t1: ", result_time_search_btree1)
    print("Tempi ricerca B-albero con t=t2: ", result_time_search_btree2)
    print("Tempi ricerca B-albero con t=t3: ", result_time_search_btree3)
    print("------")
    print("Nodi inserimento ABR: ", result_node_insert_abr)
    print("Nodi inserimento B-albero t=t1: ", result_node_insert_btree1)
    print("Nodi inserimento B-albero t=t2: ", result_node_insert_btree2)
    print("Nodi inserimento B-albero t=t3: ", result_node_insert_btree3)
    print("------")
    print("Nodi ricerca ABR: ", result_node_search_abr)
    print("Nodi ricerca B-albero con t=t1: ", result_node_search_btree1)
    print("Nodi ricerca B-albero con t=t2: ", result_node_search_btree2)
    print("Nodi ricerca B-albero con t=t3: ", result_node_search_btree3)

    if not os.path.exists("tables"):
        os.makedirs("tables")

    if not os.path.exists("plots"):
        os.makedirs("plots")

    # table: insertion execution time
    columns_time_insert = [
        [i for i in range(0, len(array_test), block_size)],
        ["{:.3e}".format(res) for res in result_time_insert_abr],
        ["{:.3e}".format(res) for res in result_time_insert_btree1],
        ["{:.3e}".format(res) for res in result_time_insert_btree2],
        ["{:.3e}".format(res) for res in result_time_insert_btree3],
    ]
    headers = ("Nr elementi", "ABR", "B-albero (t = t1)", "B-albero (t = t2)", "B-albero (t = t3)")

    drawTable(columns_time_insert, headers, "tabella1")
    plt.show()

    # table: insertion nodes
    columns_node_insert = [
        [i for i in range(0, len(array_test), block_size)],
        ["{:.3e}".format(res) for res in result_node_insert_abr],
        ["{:.3e}".format(res) for res in result_node_insert_btree1],
        ["{:.3e}".format(res) for res in result_node_insert_btree2],
        ["{:.3e}".format(res) for res in result_node_insert_btree3],
    ]

    drawTable(columns_node_insert, headers, "tabella2")
    plt.show()

    # table: search execution time
    columns_time_search = [
        [i for i in range(0, len(array_test), block_size)],
        ["{:.3e}".format(res) for res in result_time_search_abr],
        ["{:.3e}".format(res) for res in result_time_search_btree1],
        ["{:.3e}".format(res) for res in result_time_search_btree2],
        ["{:.3e}".format(res) for res in result_time_search_btree3],
    ]

    drawTable(columns_time_search, headers, "tabella3")
    plt.show()

    # table: search nodes
    columns_node_search = [
        [i for i in range(0, len(array_test), block_size)],
        ["{:.3e}".format(res) for res in result_node_search_abr],
        ["{:.3e}".format(res) for res in result_node_search_btree1],
        ["{:.3e}".format(res) for res in result_node_search_btree2],
        ["{:.3e}".format(res) for res in result_node_search_btree3],
    ]

    drawTable(columns_node_search, headers, "tabella4")
    plt.show()

    # Plots
    x = np.linspace(0, len(array_test), len(array_test) // block_size)  # asse x

    # ABR plot
    drawPlot_time(x, result_time_insert_abr, "Inserimento ABR: tempi di esecuzione", "grafico1")
    drawPlot_time(x, result_time_search_abr, "Ricerca ABR: tempi di esecuzione", "grafico2")
    drawPlot_node(x, result_node_insert_abr, "Inserimento ABR: nodi visitati", "grafico3")
    drawPlot_node(x, result_node_search_abr, "Rircerca ABR: nodi visitati", "grafico4")

    #BTree plots
    draw3Plot_time(x, result_time_insert_btree1, result_time_insert_btree2,
                   result_time_insert_btree3, "Inserimento B-albero: tempi di esecuzione", "grafico5")
    draw3Plot_node(x, result_node_insert_btree1, result_node_insert_btree2,
                   result_node_insert_btree3, "Inserimento B-albero: nodi visitati", "grafico6")
    draw3Plot_time(x, result_time_search_btree1, result_time_search_btree2,
                   result_time_search_btree3, "Ricerca B-albero: tempi di esecuzione", "grafico7")
    draw3Plot_node(x, result_node_search_btree1, result_node_search_btree2,
                   result_node_search_btree3, "Ricerca B-albero: nodi visitati", "grafico8")

    # insertion execution time plot
    draw4Plot_time(x, result_time_insert_abr, result_time_insert_btree1, result_time_insert_btree2,
                   result_time_insert_btree3, "Inserimento: tempi di esecuzione", "grafico9")
    # insertion nodes plot
    draw4Plot_node(x, result_node_insert_abr, result_node_insert_btree1, result_node_insert_btree2,
                   result_node_insert_btree3, "Inserimento: nodi visitati", "grafico10")
    # search execution time plot
    draw4Plot_time(x, result_time_search_abr, result_time_search_btree1, result_time_search_btree2,
                   result_time_search_btree3, "Ricerca: tempi di esecuzione", "grafico11")
    # search nodes plot
    draw4Plot_node(x, result_node_search_abr, result_node_search_btree1, result_node_search_btree2,
                   result_node_search_btree3, "Ricerca: nodi visitati", "grafico12")


if __name__ == '__main__':
    num_iter_test = 100
    main()
