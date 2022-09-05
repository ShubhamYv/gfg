class Solution
{
    //Function to return list of integers that form the boundary 
    //traversal of the matrix in a clockwise manner.
    static ArrayList<Integer> boundaryTraversal(int mat[][], int n, int m)
    {
        // code here 
         ArrayList<Integer> list = new ArrayList<Integer>();
        if(n==1){
            for(int i=0;i<m;i++){
                list.add(mat[0][i]);
            }
        }
         else if(m==1){
            for(int i=0;i<n;i++){
                list.add(mat[i][0]);
            }
        }
         else{
                for(int i=0;i<m;i++){
                list.add(mat[0][i]);
            }
                for(int i=1;i<n;i++){
                list.add(mat[i][m-1]);
            }
                for(int i=m-2;i>=0;i--){
                list.add(mat[n-1][i]);
            }
                 for(int i=n-2;i>=1;i--){
                list.add(mat[i][0]);
            }
            
         }
            return list ;
    }
}
