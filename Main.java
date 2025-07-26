import java.util.*;
public class Main
{
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
        System.out.print("Enter Message : ");
		String s=sc.next();
        System.out.print("Enter Number : ");
		int n=sc.nextInt();
		String encrypted=Convert(s,n);
		String Decrypted=Convert(encrypted,-n);
		System.out.println("Encrypted Message : "+" "+encrypted);
		System.out.println("Decrypted Message : "+" "+Decrypted);
	}
	public static String Convert(String s,int n){
	   StringBuilder result=new StringBuilder();
	    for(char ch:s.toCharArray()){
	        if(Character.isUpperCase(ch)){
                char p=(char)('A'+(ch-'A'+n+26)%26);
                result.append(p);
            }
            else if(Character.isLowerCase(ch)){
                char p=(char)('a'+(ch-'a'+n+26)%26);
                result.append(p);
            }
            else{
                result.append(ch);
            }
	    }
	    return result.toString();
	}
}
