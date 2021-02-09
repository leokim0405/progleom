package example;

import java.io.IOException;

public class quiz_input {

	public static void main(String[] args) throws IOException {
		char input1 = (char)System.in.read();
		System.out.println("out is : " + (int)(input1 - 48));

	}

}
