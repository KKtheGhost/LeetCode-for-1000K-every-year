/*Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
 ^
9|
8|  █         █
7|  █         █   █
6|  █ █       █   █
5|  █ █   █   █   █
4|  █ █   █ █ █   █
3|  █ █   █ █ █ █ █
2|  █ █ █ █ █ █ █ █
1|█ █ █ █ █ █ █ █ █
0 ￣￣￣￣￣￣￣￣￣￣￣￣> 

The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49 */

/*天才级别的C方案，以后学号C再来看，运行时间16ms*/
int min(int a, int b) { return a < b ? a : b; }
int max(int a, int b) { return a > b ? a : b; }

int maxArea(int* height, int heightSize)
{
    int max_area = 0, front = 0, back = heightSize - 1;
    
    while (front != back) {
        int min_height = min(height[front], height[back]);
        max_area = max((back - front) * min_height, max_area);
        if (height[front] == min_height) front++; else back--;
    }
    
    return max_area;
}