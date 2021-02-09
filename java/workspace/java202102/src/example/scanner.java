package example;

import java.util.Scanner;

public class scanner {

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		String name;
		int age;
		
		double doubleData = in.nextDouble();
		byte byteData = in.nextByte();
		short shortDAta = in.nextShort();
		float floatAte = in.nextFloat();
		
		
		System.out.print("name input : ");
		name = in.next();
		
		System.out.println("age input : ");
		age = in.nextInt();
		
		
		System.out.println("name : " + name);
		System.out.println("age : "+ age);
		
		
		// import 추가 단축 명령 : ctrl + shift + O
	}

}
