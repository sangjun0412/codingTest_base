
import java.util.Scanner;

public class Main {

	public static void main(String[] args)  {
		
		Scanner sc = new Scanner(System.in);
		
		int N = sc.nextInt();
		int[][] xy = new int[N][2];
		
		
		for(int i = 0 ; i < N ; i++) {
			 xy[i][0] = sc.nextInt();
			 xy[i][1] = sc.nextInt();
			
		}
		
		for(int j = 0 ;j< N ; j++) {
			int rank = 1;
			for(int i = 0 ;i <N ; i++) {
				if(j==i) {
					continue;
				}
				if(xy[i][0]> xy[j][0] && xy[i][1] > xy[j][1]) {
					rank++;
				}
			}
			System.out.print(rank + " ");
		}
		
		
	
		sc.close();
	}

}
