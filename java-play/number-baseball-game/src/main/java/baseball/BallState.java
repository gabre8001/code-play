package baseball;

public class BallState {
    /**
     * 사용자가 입력한 숫자와 정답을 비교한 결과를 저장하기 위한 클래스
     */
    int strike;
    int ball;

    public void setStrike(int strike) {
        this.strike = strike;
    }

    public int getStrike() {
        return strike;
    }

    public void setBall(int ball) {
        this.ball = ball;
    }

    public int getBall() {
        return ball;
    }

    public boolean isNothing() {
        if (strike == 0 && ball == 0) {
            return true;
        }
        return false;
    }

    public boolean isOut() {
        if (strike == 3) {
            return true;
        }
        return false;
    }
}
