from queue import PriorityQueue

class Graph:
    def __init__(self):
        self.adj_list={}                                                    #{node:(adjNode,wt)} undirected
        self.dir_list={}                                                 #{node:(adjNode,wt)} directed
        self.sum=0

    def update_list(self,u:int,v:int,wt:int):
        if u in self.adj_list:
            self.adj_list[u].append((v, wt))
        else:
            self.adj_list[u] = [(v, wt)]

        if v in self.adj_list:
            self.adj_list[v].append((u, wt))
        else:
            self.adj_list[v] = [(u, wt)]

        if u in self.dir_list:
            self.dir_list[u].append((v,wt))
        else:
            self.dir_list[u] = [(v,wt)]

    def checkConnected(self):
        vis={}
        def dfs(src:int):
            vis[src]=1

            for nbrs in self.adj_list[src]:
                adjNode=nbrs[0]

                if adjNode not in vis.keys():
                    dfs(adjNode)

        
        src=next(iter(self.adj_list))
        dfs(src)
        
        for node in self.adj_list.keys():
            if node not in vis.keys():
                return False

        return True

    def MST_Generator(self):
        pq=PriorityQueue()              #{wt,node,parent}
        vis={}                          #{node,true/false(0/1)}

        src=next(iter(self.adj_list))

        pq.put((0,src,-1))

        mst=[]                          #{node,parent,wt}

        self.sum=0

        while not pq.empty():
            wt,node,parent=pq.get()

            # print(f"{node} {parent} {wt}")

            if node in vis.keys():
                continue
            
            vis[node]=1
            self.sum+=wt
            if parent!=-1:
                mst.append((node,parent,wt))

            for nbrs in self.adj_list[node]:
                adjNode,adj_wt=nbrs
                # print(f"{adjNode} {adj_wt}")

                if adjNode not in vis.keys():
                    pq.put((adj_wt,adjNode,node))

        return self.sum,mst


    
if __name__=="__main__":
    g=Graph()
    g.update_list(0,1,2)
    g.update_list(1,2,3)
    # g.update_list(1,3,5)
    # g.update_list(2,3,2)
    g.update_list(3,4,7)
    g.update_list(2,4,6)

    connected=g.checkConnected()

    if connected==True:
        print("connected")
        sum,mst=g.MST_Generator()
        print("u v wt")
        print(len(mst))
        for i in mst:
            print(f"{i[0]} {i[1]} {i[2]}")

        print(f"sum {sum}")
    else:
        print("not connected")







