package baseball;

public class PrintGame {
    /**
     * 사용자에게 게임 진행에 관련한 안내를 하기위한 클래스
     */

    public void printUserInput() {
        System.out.print("숫자를 입력해 주세요: ");
    }

    public void printBallState(BallState ball) {
        if (ball.getStrike() != 0 && ball.getBall() != 0) {
            System.out.println(ball.getStrike() + "스트라이크 " + ball.getBall() + "볼");
            return;
        }
        if (ball.getStrike() != 0 && ball.getBall() == 0) {
            System.out.println(ball.getStrike() + "스트라이크");
            return;
        }
        if (ball.getStrike() == 0 && ball.getBall() != 0) {
            System.out.println(ball.getBall() + "볼");
            return;
        }
        if (ball.isNothing()) {
            System.out.println("낫싱");
            return;
        }
    }

    public void printEndGame() {
        System.out.println("3개의 숫자를 모두 맞히셨습니다! 게임 끝");
    }

    public void printCheckExitGame() {
        System.out.println("게임을 새로 시작하려면 1, 종료하려면 2를 입력하세요.");
    }

    public void printError(String message) {
        System.out.println("[ERROR] " + message);
    }

}
