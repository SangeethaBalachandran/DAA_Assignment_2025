// Sample code file for Batch Template Q1
import java.util.*;

class Item {
    int weight, value;
    Item(int weight, int value) {
        this.weight = weight;
        this.value = value;
    }
}

class Node {
    int level;
    int profit;
    int weight;
    float bound;
    Node(int level, int profit, int weight, float bound) {
        this.level = level;
        this.profit = profit;
        this.weight = weight;
        this.bound = bound;
    }
}

public class KnapsackBranchBound {
    static boolean cmp(Item a, Item b) {
        double r1 = (double)a.value / a.weight;
        double r2 = (double)b.value / b.weight;
        return r1 > r2;
    }

    static float bound(Node u, int n, int W, Item[] arr) {
        if (u.weight >= W)
            return 0;

        float profitBound = u.profit;
        int j = u.level + 1;
        int totweight = u.weight;

        while (j < n && totweight + arr[j].weight <= W) {
            totweight += arr[j].weight;
            profitBound += arr[j].value;
            j++;
        }

        if (j < n)
            profitBound += (W - totweight) * ((float)arr[j].value / arr[j].weight);

        return profitBound;
    }

    public static int knapsack(int W, Item[] arr, int n) {
        Arrays.sort(arr, (a, b) ->
            Double.compare((double)b.value / b.weight, (double)a.value / a.weight)
        );

        Queue<Node> Q = new LinkedList<>();
        Node u = new Node(-1, 0, 0, 0);
        Q.offer(u);

        int maxProfit = 0;

        while (!Q.isEmpty()) {
            u = Q.poll();
            if (u.level == n - 1)
                continue;

            Node v = new Node(u.level + 1, u.profit, u.weight, 0);

            v.weight = u.weight + arr[v.level].weight;
            v.profit = u.profit + arr[v.level].value;

            if (v.weight <= W && v.profit > maxProfit)
                maxProfit = v.profit;

            v.bound = bound(v, n, W, arr);

            if (v.bound > maxProfit)
                Q.offer(new Node(v.level, v.profit, v.weight, v.bound));

            // Exclude current item
            v.weight = u.weight;
            v.profit = u.profit;
            v.bound = bound(v, n, W, arr);

            if (v.bound > maxProfit)
                Q.offer(new Node(v.level, v.profit, v.weight, v.bound));
        }
        return maxProfit;
    }

    public static void main(String[] args) {
        int n = 4;
        int W = 15;
        Item[] arr = {
            new Item(2, 10),
            new Item(3, 5),
            new Item(5, 15),
            new Item(7, 7)
        };

        System.out.println("Maximum Profit = " + knapsack(W, arr, n));
    }
}
