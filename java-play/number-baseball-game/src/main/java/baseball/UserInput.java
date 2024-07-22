package baseball;

import nextstep.utils.Console;

public class UserInput {
    /**
     * 사용자로부터 숫자 3개를 입력 받아 유효성 확인하는 메소드
     * @return
     * @throws Exception
     */
    public String ball() throws Exception {
        String input = Console.readLine();
        if (input == null || input.equals("")) {
            throw new Exception("입력을 해야 합니다.");
        }
        if (input.length() != 3) {
            throw new Exception("숫자 3개를 입력해야 합니다.");
        }
        if (!checkNumber(input)) {
            throw new Exception("숫자를 입력해야 합니다.");
        }
        if (checkDup(input)) {
            throw new Exception("중복 숫자를 입력하면 안됩니다.");
        }
        return input;
    }

    private boolean checkDup(String input) {
        if (input.charAt(0) == input.charAt(1)
                || input.charAt(1) == input.charAt(2)
                || input.charAt(0) == input.charAt(2)) {
            return true;
        }
        return false;
    }

    private boolean checkNumber(String input) {
        if (input.charAt(0) < 49 || input.charAt(0) > 57
                || input.charAt(1) < 49 || input.charAt(1) > 57
                ||input.charAt(2) < 49 || input.charAt(2) > 57 ) {
            return false;
        }
        return true;
    }

    /**
     * 사용자로부터 게임 재시작을 위한 입력을 받고 유효성을 확인하는 메소드
     * @return
     * @throws Exception
     */
    public String restartGame() throws Exception {
        String input = Console.readLine();
        if (input == null || input.equals("")) {
            throw new Exception("입력을 해야 합니다.");
        }
        if (input.length() != 1) {
            throw new Exception("한글자를 입력해야 합니다.");
        }
        if (!input.equals("1") && !input.equals("2")) {
            throw new Exception("1또는 2를 입력해야합니다.");
        }
        return input;
    }
}
