#include <bits/stdc++.h>

using namespace std;

bool dfs(vector<vector<int>> &graph, vector<bool> &vis, int at, int dest){
    vis[at] = true;
    cout << at << " ";
    if(at == dest){
        return true;
    }
    for(const auto &i : graph[at]){
        if(!vis[i]){
            if(dfs(graph, vis, i, dest)){
                return true;
            }
        }
    }
    return false;
}

bool bfs(vector<vector<int>> &graph, vector<bool> &vis, int start, int dest) {
    queue<int> q;
    q.push(start);
    vis[start] = true;

    while (!q.empty()) {
        int at = q.front();
        q.pop();

        cout << at << " ";  // Agora o nó sempre será impresso antes de qualquer verificação.

        if (at == dest) {
            return true;  
        }

        for (const auto &i : graph[at]) {
            if (!vis[i]) {
                vis[i] = true;
                q.push(i);
            }
        }
    }

    return false; 
}

int main(){
    vector<vector<int>> graph1 = {{1, 3, 4}, {0, 2}, {1, 3, 4}, {0, 2, 4}, {0, 3, 2}};
    //alterei as letras por numeros
    vector<vector<int>> graph2 = {{1, 2}, {0, 3, 4}, {0}, {1}, {2, 3}};
    //exercicio2 (criei um pessoal)
    vector<vector<int>> graph3 = {
        {1, 2},        // 0 → 1, 2
        {0, 3, 4},     // 1 → 0, 3, 4
        {0, 5, 6},     // 2 → 0, 5, 6
        {1, 7, 8},     // 3 → 1, 7, 8
        {1, 9, 10},    // 4 → 1, 9, 10
        {2, 12, 11},   // 5 → 2, 11, 12
        {2, 14, 16},   // 6 → 2, 13, 14
        {3, 15, 16},   // 7 → 3, 15, 16
        {3, 12},           // 8 → 3
        {4, 13},           // 9 → 4
        {4},           // 10 → 4
        {5},           // 11 → 5
        {5},           // 12 → 5
        {6},           // 13 → 6
        {6},           // 14 → 6
        {7},           // 15 → 7
        {7}            // 16 → 7
    };
    

    int size1 = graph1.size();
    int size2 = graph2.size();
    int size3 = graph3.size();

    vector<bool> vis1(size1, false);
    vector<bool> vis2(size2, false);
    vector<bool> vis3(size3, false);

    int source1 = 0;
    int source2 = 0;
    int source3 = 0;

    int destination1 = 2;
    int destination2 = 3;
    int destination3 = 16;
    
    cout << "grafo 1: "; 
    dfs(graph1, vis1, 0, destination1);
    cout << "\n";
    cout << "grafo 2: ";
    dfs(graph2, vis2, 0, destination2);
    cout << "\n";
    cout << "grafo 3 com dfs: ";
    dfs(graph3, vis3, 0, destination3);
    cout << "\n";
    fill(vis3.begin(), vis3.end(), false);
    cout << "grafo 3 com bfs: ";
    bfs(graph3, vis3, 0, destination3);

    return 0;
} 