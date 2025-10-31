// Language: Java
// Problem: LeetCode #55 - Jump Game
// Includes both Brute Force and Greedy solutions

class JumpGame {

    // ---------------- Brute Force ----------------
    public static boolean canJumpBruteForce(int[] nums, int index) {
        // Base case: reached or passed last index
        if (index >= nums.length - 1) return true;

        int maxJump = nums[index];
        for (int step = 1; step <= maxJump; step++) {
            if (canJumpBruteForce(nums, index + step))
                return true;
        }
        return false;
    }

    // ---------------- Optimal Greedy ----------------
    public static boolean canJumpGreedy(int[] nums) {
        int reachable = 0;
        for (int i = 0; i < nums.length; i++) {
            if (i > reachable)
                return false;
            reachable = Math.max(reachable, i + nums[i]);
        }
        return true;
    }

    public static void main(String[] args) {
        int[] nums1 = {2, 3, 1, 1, 4};
        int[] nums2 = {3, 2, 1, 0, 4};

        System.out.println("Brute Force:");
        System.out.println(canJumpBruteForce(nums1, 0)); // true
        System.out.println(canJumpBruteForce(nums2, 0)); // false

        System.out.println("Greedy:");
        System.out.println(canJumpGreedy(nums1)); // true
        System.out.println(canJumpGreedy(nums2)); // false
    }
}
