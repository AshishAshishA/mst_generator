from django.shortcuts import render
from .graph_mst import Graph

global g
g=Graph()

def graph_with_mst(request):
    
    if request.method=="POST":
        u=int(request.POST.get('u'))
        v=int(request.POST.get('v'))
        wt=int(request.POST.get('wt'))


        g.update_list(u,v,wt)
        
        if g.checkConnected():
            sum,mst=g.MST_Generator()

            set={-1}
            node_labels=[]


            for edge in mst:
                for i in range (2):
                    if edge[i] not in set:
                        set.add(edge[i])
                        node_labels.append({'id':edge[i],'label':'Node '+str(edge[i])})

            mst_edges = [{'from': edge[0], 'to': edge[1], 'label': str(edge[2])} for edge in mst]

            graph_edges = []

            adj_list=g.dir_list

            set.clear()
            set={-1}

            for from_node, to_nodes in adj_list.items():
                for to_node in to_nodes:
                    if (from_node,to_node[0]) not in set:
                        set.add((from_node,to_node[0]))
                        graph_edges.append({'from': from_node, 'to': to_node[0], 'label': str(to_node[1])})

            context = {
                'node_labels': node_labels,
                'mst_edges': mst_edges,
                'graph_edges': graph_edges,
                'mst':mst,
                'sum':sum
            }
            return render(request, 'mst_gen_app/graph.html', context)

        else:
            mst=[]
            graph_edges = []

            adj_list=g.dir_list

            adj_list_labels=g.adj_list

            sett={(-1,-1)}


            for from_node, to_nodes in adj_list.items():
                for to_node in to_nodes:
                    if (from_node,to_node[0]) not in sett:
                        sett.add((from_node,to_node[0]))
                        graph_edges.append({'from': from_node, 'to': to_node[0], 'label': str(to_node[1])})

            set={-1}
            node_labels=[]

            for node in adj_list_labels.keys():
                if node not in set:
                    set.add(node)
                    node_labels.append({'id':node, 'label':'Node'+str(node)})


            context = {
                'node_labels': node_labels,
                'graph_edges': graph_edges,
                'mst':mst,
                'sum':0,
            }
            return render(request, 'mst_gen_app/graph.html', context)
    return render(request, 'mst_gen_app/graph.html', {})



def my_graph_view(request):
    # Sample data (replace this with your actual data fetching logic)
    node_labels = [
        {'id': 0, 'label': 'Node 0'},
        {'id': 1, 'label': 'Node 1'},
        {'id': 2, 'label': 'Node 2'},
        {'id': 3, 'label': 'Node 3'}
    ]

    adj_list = {
        0: [(1,4), (2,5)],
        1: [(0,3), (2,6), (3,8)],
        2: [(0,1), (1,2), (3,9)],
        3: [(1,1), (2,9)]
    }

    edges = []
    for from_node, to_nodes in adj_list.items():
        for to_node in to_nodes:
            edges.append({'from': from_node, 'to': to_node[0], 'label': str(to_node[1])})

    context = {'node_labels': node_labels, 'edges': edges}
    return render(request, 'mst_gen_app/graph.html', context)
