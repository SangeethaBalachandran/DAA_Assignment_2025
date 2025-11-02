import java.util.*;

public class MajorityElement {

    public static int MajorityElementFinder(int[] arr) {
        int n = arr.length;
        int count = 1, element = arr[0];
        for (int i = 1; i < n; i++) {
            if (count == 0) {
                element = arr[i];
                count++;
            } else if (arr[i] == element) {
                count++;
            } else {
                count--;
            }
        }
        return element;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter the size of the array: ");
        int n = sc.nextInt();
        int[] arr = new int[n];

        System.out.println("Enter " + n + " elements:");
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        int majority = MajorityElementFinder(arr);
        System.out.println("Majority Element: " + majority);

        sc.close();
    }
}