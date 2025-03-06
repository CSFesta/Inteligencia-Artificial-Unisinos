grafo 1: 0 1 2 
grafo 2: 0 1 3
grafo 3 com dfs: 0 1 3 7 15 16
grafo 3 com bfs: 0 1 2 3 4 5 6 7 8 9 10 12 11 14 16

Para o exercício 2: o dfs acabou sendo mais eficiente, pois ele encontrou mais rapidamente o destination, porém isso não necessariamente significa que o dfs é melhor que o bfs num contexto geral, visto que ambos tem a mesma complexidade de tempo.

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