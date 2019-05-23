#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <set>
#include <unordered_set>
#include <map>
#include <unordered_map>

const long long INF = -1;

struct Edge
{
    int to;
    float w;
    int n;
};

template<typename T>
struct Queue
{
private:
    std::vector<T> a;
    void siftUp(int pos);
    void siftDown(int pos);
public:
    Queue() {}
    Queue(size_t s) { a.reserve(s); }
    void push(const T& x);
    T top() const;
    void pop();
    bool empty() { return a.empty(); }
};

template<typename T>
void Queue<T>::siftDown(int pos)
{
    while (2 * pos + 1 < a.size()) {
        int left = 2 * pos + 1;
        int right = 2 * pos + 2;
        int to_swap = left;
        if (right < a.size() && a[right] < a[left])
            to_swap = right;
        if (a[pos] <= a[to_swap])
            break;
        std::swap(a[pos], a[to_swap]);
        pos = to_swap;
    }
}

template<typename T>
void Queue<T>::siftUp(int pos)
{
    while (a[pos] < a[(pos - 1) / 2]) {
        std::swap(a[pos], a[(pos - 1) / 2]);
        pos = (pos - 1) / 2;
    }
}

template<typename T>
T Queue<T>::top() const
{
    return a[0];
}

template<typename T>
void Queue<T>::pop()
{
    a[0] = a.back();
    a.pop_back();
    siftDown(0);
}

template<typename T>
void Queue<T>::push(const T& x)
{
    a.push_back(x);
    siftUp(a.size() - 1);
}
using Graph = std::vector<std::vector<Edge>>;

void dijkstra(const Graph& g, std::vector<std::pair<float, float>>& dist, std::vector<std::pair<int, int>>& parent, int start)
{
    //std::priority_queue<std::tuple<int, int>> q;
    Queue<std::tuple<float, float>> q(g.size());
    q.push({0, start});
    dist[start] = {0, 0};
    while (!q.empty()) {
        auto [d, v] = q.top();
        q.pop();
        for (auto e : g[v])
        {
            if (dist[e.to].first == INF || dist[e.to].first > dist[v].first + e.w || (dist[e.to].first == dist[v].first + e.w && dist[e.to].second > e.w)) {
                dist[e.to] = {dist[v].first + e.w, e.w};
                parent[e.to] = {v, e.n};
                q.push({dist[v].first + e.w, e.to});
            }
        }
    }
}

int main()
{
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int n, m;
    std::cin >> n >> m;
    Graph g(n);
    std::vector<float> edges_weight(m);
    for (int i = 0; i < m; i++) {
        int u, v; float w;
        std::cin >> u >> v >> w;
        g[u - 1].push_back({v - 1, w, i});
        g[v - 1].push_back({u - 1, w, i});
        edges_weight[i] = w;
    }
    int u;
    std::cin >> u;
    --u;
    std::vector<std::pair<float, float>> dist(n, {INF, INF});
    std::vector<std::pair<int, int>> parent(n, {-1, -1});
    dijkstra(g, dist, parent, u);
    /*
    for (auto e : dist)
        std::cerr << "{" << e.first << ", " << e.second << "} ";
    std::cerr << "\n";
    for (auto e : parent)
        std::cerr << "{" << e.first << ", " << e.second << "} ";
    std::cerr << "\n";
    */

    std::vector<int> taken;
    taken.reserve(n - 1);
    float sum = 0;
    for (auto p : parent) {
        if (p.second != -1) {
            sum += edges_weight[p.second];
            taken.push_back(p.second + 1);
        }
    }
    std::cout << sum << "\n";
    for (auto i : taken) {
        std::cout << i << " ";
    }
    return 0;
}

