package baseball;

public class Referee {
    /**
     * 세자리 숫자를 정답과 비교하여 결과를 알려주는 클래스
     */
    private String answer;

    public void setRandomNumber(String randomNumber) {
        answer = randomNumber;
    }

    /**
     * 스트라이크를 찾기위한 메소드
     * @param in
     * @return int
     */
    public int checkStrike(String in) {
        int result = 0;
        for (int i = 0; i < 3; i++) {
            result += checkStrikeAt(i, in.charAt(i), i, answer.charAt(i));
        }
        return result;
    }

    private int checkStrikeAt(int i, char c1, int j, char c2) {
        if (i == j && c1 == c2) {
            return 1;
        }
        return 0;
    }

    /**
     * 볼을 찾기위한 메소드
     * @param in
     * @return int
     */
    public int checkBall(String in) {
        int result = 0;
        for (int i = 0; i < 3; i++) {
            result += checkBallI(in, i);
        }
        return result;
    }

    private int checkBallI(String in, int i) {
        int result = 0;
        for (int j = 0; j < 3; j++) {
            result += checkBallAt(i, in.charAt(i), j, answer.charAt(j));
        }
        return result;
    }

    private int checkBallAt(int i, char c1, int j, char c2) {
        if (i != j && c1 == c2) {
            return 1;
        }
        return 0;
    }

    /**
     * 사용자 입력값의 결과를 반환하는 메소드
     * @param in
     * @return BallState
     */
    public BallState checkBallState(String in) {
        BallState ball = new BallState();
        ball.setStrike(checkStrike(in));
        ball.setBall(checkBall(in));
        return ball;
    }

}
