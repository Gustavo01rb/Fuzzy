from turtle import color
import numpy as np
import matplotlib.pyplot as plt

class Graph:
    @staticmethod
    def multi_column_plot(line, column, title = False, width = 25, height = 17):
        plt.clf()
        fig,axs = plt.subplots(line, column,)
        fig.set_figwidth(width)
        fig.set_figheight(height)
        plt.subplots_adjust(left=0.125,
                    bottom=0.1, 
                    right=0.95, 
                    top=0.9, 
                    wspace=0.1, 
                    hspace=0.3)
        fig.subplots_adjust(top=0.95)
        if title: fig.suptitle(title,fontsize=22, fontweight ="bold")

        return fig,axs

    @staticmethod
    def format_multi_column_plot(axs,line, column, path_save, show=False, active_legend = False, yticks = np.arange(0,1.01,0.2),):
        for i in range(line):
            for j in range(column):
                if active_legend: axs[i,j].legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),fancybox=True, shadow=True, ncol=8, prop={'size': 18})
                axs[i,j].set_yticks(yticks)
        plt.savefig(path_save)
        if show: plt.show()
        plt.clf()


    @staticmethod
    def inline_plot(data, range, path_save, title=False, fig_width = 21, fig_heigh = 12, label=False, active_legend=False,doted=999, subtitle=False, show=False,fill=False):

        plt.clf()
        fig, axs = plt.subplots(data.shape[0])
        fig.tight_layout()
        fig.subplots_adjust(top=0.9, right=0.85)
        fig.set_figwidth(fig_width)
        fig.set_figheight(fig_heigh)
        if title: fig.suptitle(title,fontsize=22, fontweight ="bold")

        for index_graph, graph in enumerate(data):
            for index_function, function in enumerate(graph):
                if not fill:
                    axs[index_graph].plot(
                        range, 
                        function, 
                        '-' if index_function < doted else '--',
                        label = label[index_graph][index_function] if label else "" 
                    )
                    continue
                if fill[index_graph][index_function]:
                    axs[index_graph].fill_between(
                        range, 
                        function,
                        '-' if index_function < doted else '--',
                        label = label[index_graph][index_function] if label else "",
                        color='tab:purple', 
                        alpha = 0.5
                    )
                else:
                    axs[index_graph].plot(
                        range, 
                        function, 
                        '-' if index_function < doted else '--',
                        label = label[index_graph][index_function] if label else "" 
                    )

            if active_legend:
                axs[index_graph].legend(loc='center left', bbox_to_anchor=(1, 0.5),prop={'size': 20})
            if subtitle:
                axs[index_graph].set_title(subtitle[index_graph], loc='left',fontsize=16, fontweight =200)
        
        plt.savefig(path_save)
        if show: plt.show()
        plt.clf()
        
