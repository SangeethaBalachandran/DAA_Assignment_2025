// Language: Java
// Problem: LeetCode #45 - Jump Game II
// Includes both Brute Force and Greedy solutions

class JumpGameII {

    // ---------------- Brute Force ----------------
    public static int jumpBruteForce(int[] nums, int index) {
        if (index >= nums.length - 1)
            return 0; // Reached the end, no more jumps

        int maxJump = nums[index];
        if (maxJump == 0)
            return Integer.MAX_VALUE; // Cannot move further

        int minJumps = Integer.MAX_VALUE;
        for (int step = 1; step <= maxJump; step++) {
            int jumps = jumpBruteForce(nums, index + step);
            if (jumps != Integer.MAX_VALUE)
                minJumps = Math.min(minJumps, 1 + jumps);
        }
        return minJumps;
    }

    // ---------------- Optimal Greedy ----------------
    public static int jumpGreedy(int[] nums) {
        int jumps = 0, currentEnd = 0, farthest = 0;
        for (int i = 0; i < nums.length - 1; i++) {
            farthest = Math.max(farthest, i + nums[i]);
            if (i == currentEnd) {
                jumps++;
                currentEnd = farthest;
            }
        }
        return jumps;
    }

    public static void main(String[] args) {
        int[] nums1 = {2, 3, 1, 1, 4};

        System.out.println("Brute Force:");
        System.out.println(jumpBruteForce(nums1, 0)); // Output: 2

        System.out.println("Greedy:");
        System.out.println(jumpGreedy(nums1)); // Output: 2
    }
}
