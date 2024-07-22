package baseball;

import java.util.HashMap;
import java.util.Map;

public class Controller {
    private Map<Enum<GameState>, Runnable> map;
    GameEvent event;
    Referee referee;
    PrintGame out;
    UserInput in;

    public Controller() {
        /**
         * 게임 상태에 따라 게임 흐름을 제어하는 클래스
         */
        event = new GameEvent();
        event.setState(GameState.INIT);
        referee = new Referee();
        out = new PrintGame();
        in = new UserInput();
        mappingController();
    }

    /**
     * 게임 상태와 그에 따라 실행할 메소드를 맵핑
     */
    private void mappingController() {
        map = new HashMap<>();
        map.put(GameState.INIT, this::initGame);
        map.put(GameState.REFEREECHECK, this::refereeCheck);
        map.put(GameState.END, this::endGame);
        map.put(GameState.CHECKRESTART, this::checkRestartGame);
        map.put(GameState.EXIT, this::exitGame);
    }

    /**
     * 세자리 숫자를 생성하여 게임 초기화하고 게임 상태를 REFEREECHECK로 변경
     * GameState.INIT 에 해당하는 메소드
     */
    public void initGame() {
        referee.setRandomNumber(ThreeDigit.get());
        event.setState(GameState.REFEREECHECK);
    }

    /**
     * 사용자에게 숫자 입력을 받고 그 숫자를 판단하여 게임 상태 변경
     * GameState.REFEREECHECK 에 해당하는 메소드
     */
    public void refereeCheck() {
        out.printUserInput();
        try {
            event.setState(GameState.REFEREECHECK);
            String input = in.ball();
            BallState ballState = referee.checkBallState(input);
            out.printBallState(ballState);
            chaeckGameOut(ballState);
        } catch (Exception e) {
            out.printError(e.getMessage());
        }
    }

    /**
     * 게임이 끝났다는 것을 알리고 게임 상태를 CHECKRESTART 변경
     * GameState.END 에 해당하는 메소드
     */
    public void endGame() {
        out.printEndGame();
        event.setState(GameState.CHECKRESTART);
    }

    /**
     * 게임 사용자에게 다시 시작할 것인지 물어보고 게임 재실행 여부 판단
     * GameState.RESTART 에 해당하는 메소드
     */
    public void checkRestartGame() {
        out.printCheckExitGame();
        try {
            event.setState(GameState.CHECKRESTART);
            String input = in.restartGame();
            event.setState(GameState.INIT);
            checkExitGame(input);
        } catch (Exception e) {
            out.printError(e.getMessage());
        }
    }

    /**
     * 3스트라이크 일때 게임 상태를 END로 변경
     * @param ballState
     */
    private void chaeckGameOut(BallState ballState) {
        if (ballState.isOut()) {
            event.setState(GameState.END);
        }
    }

    /**
     * 게임 사용자가 2를 선택 했을 때 게임 상태를 EXIT로 변경
     * @param input
     */
    private void checkExitGame(String input) {
        if (input.equals("2")) {
            event.setState(GameState.EXIT);
        }
    }

    //GameState.EXIT
    private void exitGame() {
        System.exit(0);
    }

    //맵에서 게임 상태에 해당하는 메소드를 가져와 실행
    public void run() {
        map.get(event.getState()).run();
    }
}
