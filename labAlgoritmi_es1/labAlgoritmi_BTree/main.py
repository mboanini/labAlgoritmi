import random

import numpy as np
import matplotlib.pyplot as plt
import timeit
import sys
import os

from ABR import *
from BTree import *

sys.setrecursionlimit(10000)

# Valore massimo che può essere inserito nell'array
# maxValue = 1000
# maxlength = 20


# Array di numeri random
# def randomArray(n):
  #  return np.random.randint(0, maxValue + 1, n).tolist()


def drawTable(columns: list, headers: tuple, title: str):
    fig, ax = plt.subplots(figsize=(8, 35))
    plt.title(title)

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

    fig.savefig("./tables/Tabelle.png", bbox_inches='tight')


def drawPlot_time(x, y, string):
    fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
    ax.plot(x, y, label='abr')  # Plot some data on the axes.
    ax.set_xlabel('Numero elementi')  # Add an x-label to the axes.
    ax.set_ylabel('Tempo [ms]')  # Add a y-label to the axes.
    ax.set_title(string)  # Add a title to the axes.
    plt.show()


def drawPlot_node(x, y, string):
    fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
    ax.plot(x, y, label='abr')  # Plot some data on the axes.
    ax.set_xlabel('Numero elementi')  # Add an x-label to the axes.
    ax.set_ylabel('Numero nodi')  # Add a y-label to the axes.
    ax.set_title(string)  # Add a title to the axes.
    plt.show()


def draw4Plot_time(x, y0, y1, y2, y3, string):
    fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
    ax.plot(x, y0, label='abr')  # Plot some data on the axes.
    ax.plot(x, y1, label='btree(t1)')  # Plot more data on the axes...
    ax.plot(x, y2, label='btree(t2)')  # ... and some more.
    ax.plot(x, y3, label='btree(t3)')  # ... and some more.
    ax.set_xlabel('Numero elementi')  # Add an x-label to the axes.
    ax.set_ylabel('Tempo [ms]')  # Add a y-label to the axes.
    ax.set_title(string)  # Add a title to the axes.
    ax.legend()  # Add a legend.
    plt.show()


def draw4Plot_node(x, y0, y1, y2, y3, string):
    fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
    ax.plot(x, y0, label='abr')  # Plot some data on the axes.
    ax.plot(x, y1, label='btree(t1)')  # Plot more data on the axes...
    ax.plot(x, y2, label='btree(t2)')  # ... and some more.
    ax.plot(x, y3, label='btree(t3)')  # ... and some more.
    ax.set_xlabel('Numero elementi')  # Add an x-label to the axes.
    ax.set_ylabel('Numero nodi')  # Add a y-label to the axes.
    ax.set_title(string)  # Add a title to the axes.
    ax.legend()  # Add a legend.
    plt.show()


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

        t1 = 250  # 20
        t2 = 700  # 250
        t3 = 3000  # 1000
        array_test = np.random.randint(0, 100, 10000)  # 10000
        # print(array_test)
        my_btree1 = BTree(t1)
        my_btree2 = BTree(t2)
        my_btree3 = BTree(t3)
        my_tree = ABR()
        values_inserted = []

        block_size = 100  # 100

        for j in range(0, len(array_test), block_size):
            # test per tempo di esecuzione inserimento in abr
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
            # print(it, j, j + k)
            # print("Tempo per inserimento abr: ", result_time_insert_abr_partial)
            # print("Nr nodi visitati per inserimento abr: ", result_node_insert_abr_partial)

            # test per tempo di esecuzione inserimento in btree
            start_time = timeit.default_timer()
            for k in range(0, block_size):
                my_btree1.btree_insert(array_test[j + k])
            end_time = timeit.default_timer()
            result_time_insert_btree1_partial.append((end_time - start_time) * 1000)
            result_node_insert_btree1_partial.append(my_btree1.get_node_read() + my_btree1.get_node_written())
            my_btree1.node_read = 0
            my_btree1.node_written = 0

            # my_btree1.btree_print(my_btree1.root)
            # print("Tempo per inserimento btree con t=t1: ", result_time_insert_btree1_partial)
            # print("Nr nodi visitati per inserimento btree con t=t1: ", result_node_insert_btree1_partial)

            start_time = timeit.default_timer()
            for k in range(0, block_size):
                my_btree2.btree_insert(array_test[j + k])
            end_time = timeit.default_timer()
            result_time_insert_btree2_partial.append((end_time - start_time) * 1000)
            result_node_insert_btree2_partial.append(my_btree2.get_node_read() + my_btree2.get_node_written())
            my_btree2.node_read = 0
            my_btree2.node_written = 0

            # my_btree2.btree_print(my_btree1.root)
            # print("Tempo per inserimento btree con t=t2: ", result_time_insert_btree2_partial)
            # print("Nr nodi visitati per inserimento btree con t=t2: ", result_node_insert_btree2_partial)

            start_time = timeit.default_timer()
            for k in range(0, block_size):
                my_btree3.btree_insert(array_test[j + k])
            end_time = timeit.default_timer()
            result_time_insert_btree3_partial.append((end_time - start_time) * 1000)
            result_node_insert_btree3_partial.append(my_btree3.get_node_read() + my_btree3.get_node_written())
            my_btree3.node_read = 0
            my_btree3.node_written = 0

            # my_btree3.btree_print(my_btree1.root)
            # print("Tempo per inserimento btree con t=t3: ", result_time_insert_btree3_partial)
            # print("Nr nodi visitati per inserimento btree con t=t3: ", result_node_insert_btree3_partial)

            start_time = timeit.default_timer()
            for k in range(0, block_size):
                my_tree.ABR_search(random.choice(values_inserted))
            end_time = timeit.default_timer()
            result_time_search_abr_partial.append((end_time - start_time) * 1000)
            result_node_search_abr_partial.append(my_tree.get_node_read() + my_tree.get_node_written())
            my_tree.node_read = 0
            my_tree.node_written = 0

            # print("Tempo per ricerca abr: ", result_time_search_abr_partial)
            # print("Nr nodi visitati per ricerca abr: ", result_node_search_abr_partial)

            start_time = timeit.default_timer()
            for k in range(0, block_size):
                my_btree1.btree_search(random.choice(values_inserted))
            end_time = timeit.default_timer()
            result_time_search_btree1_partial.append((end_time - start_time) * 1000)
            result_node_search_btree1_partial.append(my_btree1.get_node_read() + my_btree1.get_node_written())
            my_tree.node_read = 0
            my_tree.node_written = 0

            # my_btree1.btree_print(my_btree1.root)
            # print("Tempo per ricerca btree con t=t1: ", result_time_search_btree1_partial)
            # print("Nr nodi visitati per ricerca btree con t=t1: ", result_node_search_btree1_partial)

            start_time = timeit.default_timer()
            for k in range(0, block_size):
                my_btree2.btree_search(random.choice(values_inserted))
            end_time = timeit.default_timer()
            result_time_search_btree2_partial.append((end_time - start_time) * 1000)
            result_node_search_btree2_partial.append(my_btree2.get_node_read() + my_btree2.get_node_written())
            my_tree.node_read = 0
            my_tree.node_written = 0

            # my_btree2.btree_print(my_btree2.root)
            # print("Tempo per ricerca btree con t=t2: ", result_time_search_btree2_partial)
            # print("Nr nodi visitati per ricerca btree con t=t3: ", result_node_search_btree2_partial)

            start_time = timeit.default_timer()
            for k in range(0, block_size):
                my_btree3.btree_search(random.choice(values_inserted))
            end_time = timeit.default_timer()
            result_time_search_btree3_partial.append((end_time - start_time) * 1000)
            result_node_search_btree3_partial.append(my_btree3.get_node_read() + my_btree3.get_node_written())
            my_tree.node_read = 0
            my_tree.node_written = 0

            # my_btree3.btree_print(my_btree3.root)
            # print("Tempo per ricerca btree con t=t3: ", result_time_search_btree3_partial)
            # print("Nr nodi visitati per ricerca btree con t=t3: ", result_node_search_btree3_partial)

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

    print("Tempi inserimento abr: ", result_time_insert_abr)
    print("Tempi inserimento btree t=t1: ", result_time_insert_btree1)
    print("Tempi inserimento btree t=t2: ", result_time_insert_btree2)
    print("Tempi inserimento btree t=t3: ", result_time_insert_btree3)
    print("------")
    print("Tempi ricerca abr: ", result_time_search_abr)
    print("Tempi ricerca btree con t=t1: ", result_time_search_btree1)
    print("Tempi ricerca btree con t=t2: ", result_time_search_btree2)
    print("Tempi ricerca btree con t=t3: ", result_time_search_btree3)
    print("------")
    print("Nodi inserimento abr: ", result_node_insert_abr)
    print("Nodi inserimento btree t=t1: ", result_node_insert_btree1)
    print("Nodi inserimento btree t=t2: ", result_node_insert_btree2)
    print("Nodi inserimento btree t=t3: ", result_node_insert_btree3)
    print("------")
    print("Nodi ricerca abr: ", result_node_search_abr)
    print("Nodi ricerca btree con t=t1: ", result_node_search_btree1)
    print("Nodi ricerca btree con t=t2: ", result_node_search_btree2)
    print("Nodi ricerca btree con t=t3: ", result_node_search_btree3)

    if not os.path.exists("tables"):
        os.makedirs("tables")

    # Tabella ABR
    columns_abr = [
        [i for i in range(0, len(array_test), block_size)],
        ["{:.3e}".format(res) for res in result_time_insert_abr],
        ["{:.3e}".format(res) for res in result_node_insert_abr],
        ["{:.3e}".format(res) for res in result_time_search_abr],
        ["{:.3e}".format(res) for res in result_node_search_abr],
    ]

    headers_abr = ("Nr elementi", "Tempo insert", "Nodi insert", "Tempo search", "Nodi search")
    title_abr = "Albero binario di Ricerca"

    drawTable(columns_abr, headers_abr, title_abr)
    plt.show()

    # Tabella Btree con t=t1
    columns_btree1 = [
        [i for i in range(0, len(array_test), block_size)],
        ["{:.3e}".format(res) for res in result_time_insert_btree1],
        ["{:.3e}".format(res) for res in result_node_insert_btree1],
        ["{:.3e}".format(res) for res in result_time_search_btree1],
        ["{:.3e}".format(res) for res in result_node_search_btree1],
    ]

    headers_btree1 = ("Nr elementi", "Tempo insert", "Nodi insert", "Tempo search", "Nodi search")
    title_btree1 = "B Albero con t = t1"

    drawTable(columns_btree1, headers_btree1, title_btree1)
    plt.show()

    # Tabella Btree con t=t2
    columns_btree2 = [
        [i for i in range(0, len(array_test), block_size)],
        ["{:.3e}".format(res) for res in result_time_insert_btree2],
        ["{:.3e}".format(res) for res in result_node_insert_btree2],
        ["{:.3e}".format(res) for res in result_time_search_btree2],
        ["{:.3e}".format(res) for res in result_node_search_btree2],
    ]

    headers_btree2 = ("Nr elementi", "Tempo insert", "Nodi insert", "Tempo search", "Nodi search")
    title_btree2 = "B Albero con t = t2"

    drawTable(columns_btree2, headers_btree2, title_btree2)
    plt.show()

    # Tabella Btree con t=t3
    columns_btree3 = [
        [i for i in range(0, len(array_test), block_size)],
        ["{:.3e}".format(res) for res in result_time_insert_btree3],
        ["{:.3e}".format(res) for res in result_node_insert_btree3],
        ["{:.3e}".format(res) for res in result_time_search_btree3],
        ["{:.3e}".format(res) for res in result_node_search_btree3],
    ]

    headers_btree3 = ("Nr elementi", "Tempo insert", "Nodi insert", "Tempo search", "Nodi search")
    title_btree3 = "B Albero con t = t3"

    drawTable(columns_btree3, headers_btree3, title_btree3)
    plt.show()

    # Grafici
    x = np.linspace(0, len(array_test), block_size)  # Sample data.
    # x = np.arange(0, len(array_test) * block_size, block_size)

    drawPlot_time(x, result_time_insert_abr, "Tempi di inserimento abr")
    drawPlot_time(x, result_time_insert_btree1, "Tempi di inserimento btree con t=t1")
    drawPlot_time(x, result_time_insert_btree2, "Tempi di inserimento btree con t=t2")
    drawPlot_time(x, result_time_insert_btree3, "Tempi di inserimento btree con t=t3")

    drawPlot_time(x, result_time_search_abr, "Tempi di ricerca abr")
    drawPlot_time(x, result_time_search_btree1, "Tempi di ricerca btree con t=t1")
    drawPlot_time(x, result_time_search_btree2, "Tempi di ricerca btree con t=t2")
    drawPlot_time(x, result_time_search_btree3, "Tempi di ricerca btree con t=t3")

    drawPlot_node(x, result_node_insert_abr, "Numero nodi inserimento abr")
    drawPlot_node(x, result_node_insert_btree1, "Numero nodi inserimento btree con t=t1")
    drawPlot_node(x, result_node_insert_btree2, "Numero nodi inserimento btree con t=t2")
    drawPlot_node(x, result_node_insert_btree3, "Numero nodi inserimento btree con t=t3")

    drawPlot_node(x, result_node_search_abr, "Numero nodi ricerca abr")
    drawPlot_node(x, result_node_search_btree1, "Numero nodi ricerca btree con t=t1")
    drawPlot_node(x, result_node_search_btree2, "Numero nodi ricerca btree con t=t2")
    drawPlot_node(x, result_node_search_btree3, "Numero nodi ricerca btree con t=t3")

    # Grafico tempi insert
    draw4Plot_time(x, result_time_insert_abr, result_time_insert_btree1, result_time_insert_btree2,
                   result_time_insert_btree3, "Tempi di inserimento (prova)")
    # Grafico nodi insert
    draw4Plot_node(x, result_node_insert_abr, result_node_insert_btree1, result_node_insert_btree2,
                   result_node_insert_btree3, "Nodi inserimento (prova)")
    # Grafico tempi search
    draw4Plot_time(x, result_time_search_abr, result_time_search_btree1, result_time_search_btree2,
                   result_time_search_btree3, "Tempi di ricerca (prova)")
    # Grafico nodi search
    draw4Plot_node(x, result_node_search_abr, result_node_search_btree1, result_node_search_btree2,
                   result_node_search_btree3, "Nodi ricerca (prova)")


if __name__ == '__main__':
    num_iter_test = 10
    main()
