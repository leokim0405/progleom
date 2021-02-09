package example;

import java.io.IOException;

public class input_ex {

	public static void main(String[] args) throws IOException {
		System.out.print("데이터 입력 : ");
		int intdata = System.in.read();
		System.out.print("출력 : " + (char)intdata);
		
//		int data = System.in.read();
//		System.out.println("data = " + (char)data);
		
		/*
		 * read를 연속으로 사용하면 아래와 같은 결과가 나옴
		 * 첫번째 입/출력은 잘 되지만, 두번째 입력은 없고, 출력은 되지만 나오는 값이 없음
		 * system.in.read();systemc.in.read(); 두번을 사용해서 문자를 연속으로 입력 받는 것을 해결할 수 있음
		 */
	}

}
