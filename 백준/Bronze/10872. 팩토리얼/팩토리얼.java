
import java.util.Scanner;


public class Main {
	static int factorial(int num) {
		if(num <= 1) {
			return 1;
		}
		
		else {
			return	num * factorial(num-1);
		}
	}
	public static void main(String[] args) {
	    Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();	
		System.out.print( factorial(num) );
		sc.close();
	}

}
