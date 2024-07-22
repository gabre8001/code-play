package baseball;

import nextstep.utils.Randoms;

public class ThreeDigit {

    /**
     * 중복하지 않는 세자리 숫자를 얻기 위한 메소드
     * @return string 중복하지 않는 세자리 숫자
     */
    public static String get() {
        StringBuilder sb = new StringBuilder();
        while(sb.length() < 3) {
            String num =Randoms.pickNumberInRange(1,9) + "";
            sb = addNumber(sb, num);
        }
        return sb.toString();
    }

    private static StringBuilder addNumber(StringBuilder sb, String number) {
        if (sb.indexOf(number) == -1) {
            sb.append(number);
        }
        return sb;
    }
}
