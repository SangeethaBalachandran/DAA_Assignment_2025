// Sample code file for Batch Template Q2
import java.util.*;
public class TradeLiveGreedy{
    static class Order{
        int a,b,diff;
        Order(int a,int b){
            this.a=a;
            this.b=b;
            this.diff=Math.abs(a-b);
        } }
    static int maxTip(int[] A,int[] B,int X,int Y){
        int n=A.length;
        List<Order> orders=new ArrayList<>();
        for(int i=0;i<n;i++){
           orders.add(new Order(A[i],B[i]));
        }
        orders.sort((o1,o2)->o2.diff-o1.diff);
        int totalTip=0,andyCount=0,bobCount=0;
        for(Order order:orders){
        if((order.a>=order.b&&andyCount<X)||bobCount>=Y){
                totalTip+=order.a;
                andyCount++;
            }else{
                totalTip+=order.b;
                bobCount++;
            } }
        return totalTip;
      }
      public static void main(String[] args){
          int[] A={8,7,15,19,16};
          int[] B={1,2,3,4,5};
          int X=3,Y=3;
          int result=maxTip(A,B,X,Y);
          System.out.println("Maximum Total Tip (Greedy Approach): "+result);
      }}

