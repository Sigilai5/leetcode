import java.util.LinkedList;
import java.util.Queue;

class Solution {
    public int maxDepth(TreeNode root) {
        if (root == null) {
            return 0;
        }

        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(root);
        int maxDepth = 0;

        while (!queue.isEmpty()) {
            int levelSize = queue.size(); // Store the current size of the queue

            // Process all nodes at the current level
            for (int i = 0; i < levelSize; i++) {
                TreeNode node = queue.poll();

                if (node.left != null) {
                    queue.add(node.left);
                }

                if (node.right != null) {
                    queue.add(node.right);
                }
            }

            maxDepth++; // Increment depth after processing all nodes at the current level
        }

        return maxDepth;
    }
}
