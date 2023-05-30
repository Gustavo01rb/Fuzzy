from turtle import color
import numpy as np
import matplotlib.pyplot as plt

class Graph:
    @staticmethod
    def multi_column_plot(line, column, title=False, width=25, height=17):
        """
        Cria um gráfico com múltiplas colunas.

        Parâmetros:
        - line: int
          Número de linhas do gráfico.
        - column: int
          Número de colunas do gráfico.
        - title: str ou False, opcional
          Título do gráfico. Se False, nenhum título será exibido.
        - width: int, opcional
          Largura da figura em polegadas.
        - height: int, opcional
          Altura da figura em polegadas.

        Retorno:
        - fig: matplotlib.figure.Figure
          A figura do gráfico.
        - axs: np.ndarray
          Um array de objetos Axes, representando os subplots do gráfico.
        """
        plt.clf()
        fig, axs = plt.subplots(line, column)
        fig.set_figwidth(width)
        fig.set_figheight(height)
        plt.subplots_adjust(left=0.125, bottom=0.1, right=0.95, top=0.9, wspace=0.1, hspace=0.3)
        fig.subplots_adjust(top=0.95)
        if title:
            fig.suptitle(title, fontsize=22, fontweight="bold")

        return fig, axs

    @staticmethod
    def format_multi_column_plot(axs, line, column, path_save, show=False, active_legend=False, yticks=np.arange(0, 1.01, 0.2)):
        """
        Formata o gráfico com múltiplas colunas.

        Parâmetros:
        - axs: np.ndarray
          Um array de objetos Axes, representando os subplots do gráfico.
        - line: int
          Número de linhas do gráfico.
        - column: int
          Número de colunas do gráfico.
        - path_save: str
          Caminho para salvar o gráfico.
        - show: bool, opcional
          Se True, exibe o gráfico na tela. Caso contrário, não é exibido.
        - active_legend: bool, opcional
          Se True, ativa a legenda nos subplots.
        - yticks: np.ndarray, opcional
          Array de valores para os marcadores do eixo y.

        Retorno:
        - None
        """
        for i in range(line):
            for j in range(column):
                if active_legend:
                    axs[i, j].legend(
                        loc='upper center', bbox_to_anchor=(0.5, -0.05), fancybox=True, shadow=True, ncol=8, prop={'size': 18})
                axs[i, j].set_yticks(yticks)
        plt.savefig(path_save)
        if show:
            plt.show()
        plt.clf()


    @staticmethod
    def inline_plot(data, path_save, range, multi_range=False, title=False, fig_width=21, fig_height=12, label=False, active_legend=False, dotted=999, subtitle=False, show=False, fill=False, yticks=np.arange(0, 1.01, 0.2), legend_size=20):
        """
        Cria um gráfico inline.

        Parâmetros:
        - data: np.ndarray
          Matriz de dados para plotagem. Cada linha representa um gráfico.
        - path_save: str
          Caminho para salvar o gráfico.
        - range: np.ndarray
          Array com os valores do eixo x.
        - multi_range: np.ndarray, opcional
          Matriz de valores do eixo x para cada linha do gráfico. Se False, usa o mesmo range para todas as linhas.
        - title: str ou False, opcional
          Título do gráfico. Se False, nenhum título será exibido.
        - fig_width: int, opcional
          Largura da figura em polegadas.
        - fig_height: int, opcional
          Altura da figura em polegadas.
        - label: bool, opcional
          Se True, exibe rótulos no gráfico.
        - active_legend: bool, opcional
          Se True, ativa a legenda no gráfico.
        - dotted: int, opcional
          Índice a partir do qual as linhas serão desenhadas como tracejadas.
        - subtitle: bool, opcional
          Se True, exibe subtítulos no gráfico.
        - show: bool, opcional
          Se True, exibe o gráfico na tela. Caso contrário, não é exibido.
        - fill: bool, opcional
          Se True, preenche a área entre as curvas do gráfico.
        - yticks: np.ndarray, opcional
          Array de valores para os marcadores do eixo y.
        - legend_size: int, opcional
          Tamanho da fonte da legenda.

        Retorno:
        - None
        """
        plt.clf()
        fig, axs = plt.subplots(data.shape[0])
        fig.tight_layout()
        fig.subplots_adjust(top=0.9, right=0.85)
        fig.set_figwidth(fig_width)
        fig.set_figheight(fig_height)
        if title:
            fig.suptitle(title, fontsize=22, fontweight="bold")

        for index_graph, graph in enumerate(data):
            for index_function, function in enumerate(graph):
                if not fill:
                    axs[index_graph].plot(
                        range if not multi_range else multi_range[index_graph],
                        function,
                        '-' if index_function < dotted else '--',
                        label=label[index_graph][index_function] if label else ""
                    )
                    continue
                if fill[index_graph][index_function]:
                    axs[index_graph].fill_between(
                        range if not multi_range else multi_range[index_graph],
                        function,
                        '-' if index_function < dotted else '--',
                        label=label[index_graph][index_function] if label else "",
                        color='tab:purple',
                        alpha=0.5
                    )
                else:
                    axs[index_graph].plot(
                        range if not multi_range else multi_range[index_graph],
                        function,
                        '-' if index_function < dotted else '--',
                        label=label[index_graph][index_function] if label else ""
                    )
            axs[index_graph].set_yticks(yticks)
            if active_legend:
                axs[index_graph].legend(loc='center left', bbox_to_anchor=(1, 0.5), prop={'size': legend_size})
            if subtitle:
                axs[index_graph].set_title(subtitle[index_graph], loc='left', fontsize=16, fontweight=200)

        plt.savefig(path_save)
        if show:
            plt.show()
        plt.clf()
