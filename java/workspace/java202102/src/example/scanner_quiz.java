package example;

import java.util.Scanner;

public class scanner_quiz {

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		
		System.out.println("name?");
		String name = in.next();
		
		System.out.println("k_score?");
		int k_score = in.nextInt();
		
		System.out.println("name : "+ name);
		System.out.println("k_Score : " + k_score);
		

	}

}
