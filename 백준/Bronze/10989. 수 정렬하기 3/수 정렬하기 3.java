
import java.io.*;
import java.util.Arrays;
import java.io.IOException;
public class Main {
	
	
	public static void main(String[] args) throws IOException{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int number = Integer.parseInt(br.readLine());
		
	
		StringBuilder sb = new StringBuilder();
		
		int[] index = new int[number];
		
		for(int i = 0; i<number; i++) {
			index[i] = Integer.parseInt(br.readLine());
		}
		
		Arrays.sort(index);
		
		for(int j = 0; j < number; j++) {
			
			sb.append(index[j]).append('\n');
			
		}
		
		System.out.println(sb);
		br.close();
		
	}
}
